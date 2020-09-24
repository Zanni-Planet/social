
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.cache import cache
from User.models import User,More

from User.logics import send_vcode



def fetch_vcode(request):
    '''发送短信验证码'''
    phonenum = request.GET.get('phonenum')
    if send_vcode(phonenum):
        return JsonResponse({'code': 0, 'data': None})
    else:
        return JsonResponse({'code': 1000, 'data': '验证码发送错误'})


def submit_vcode(request):
    '''登录'''
    data = {'code': 0,'data': None}
    if request.method == 'POST':
        phonenum = request.POST.get('phonenum')
        vcode = request.POST.get('vcode')
        # 验证验证码
        key = 'Vcode-%s' % phonenum
        code = cache.get(key)
        if code and vcode == code:
            try:
                user = User.objects.get(phonenum=phonenum)
            except User.DoesNotExist:
                user = User.objects.create(phonenum=phonenum, nickname=phonenum)
            request.session['uid'] = user.id
            data['data'] = {user.to_dict()}
        else:
            data['code'] = 1001
            data['data'] = '验证码错误'
        return JsonResponse(data)

        
def show_profile(request):
    '''查看个⼈、交友资料'''
    uid = request.session.get('uid')
    more = More.objects.get(uid=uid)
    data = {
        'code': 0,
        'data': more.to_dict()}
    return JsonResponse(data)


def update_profile(request):
    ''' 修改 个⼈资料 及 交友资料'''
    uid = request.session.get('uid')
    user = User.objects.get(pk=uid)
    more = More.objects.get(uid=uid)
    user.nickname = request.POST.get('nickname')
    user.birthday = request.POST.get('birthday')
    user.gender = request.POST.get('gender')
    user.location = request.POST.get('location')
    user.save()

    more.dating_gender = request.POST.get('dating_gender')
    more.dating_location = request.POST.get('dating_location')
    more.max_distance = request.POST.get('max_distance')
    more.min_distance = request.POST.get('min_distance')
    more.max_dating_age = request.POST.get('max_dating_age')
    more.min_dating_age = request.POST.get('min_dating_age')
    more.vibration = request.POST.get('vibration')
    more.only_matched = request.POST.get('only_matched')
    more.auto_play = request.POST.get('auto_play')
    more.save()
    data = {'code':0,'data':None}
    return JsonResponse(data)


def qn_token(request):
    pass


def qn_callback(request):
    pass
