from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from User.models import User

from libs.sms import text_send

# Create your views here.


def fetch(request):
    '''发送短信验证码'''
    phonenum = request.GET.get('phonenum')
    print(phonenum)
    code = text_send(phonenum)
    # 存储验证码到session
    print(vcode)
    request.session['code'] = code
    data = {
        'code':0,
    }
    return JsonResponse(data=data)
    # return HttpResponse('发送成功')

def login(request):
    '''登录'''
    if request.method == 'POST':
        phonenum = request.POST.get('phonenum')
        vcode = request.POST.get('vcode')
        # 验证验证码
        code = request.session.get('code')
        if vcode != code:
            pass
        user = User.objects.filter(phonenum=phonenum)
        if not user.id:
            user = User()
            user.phonenum = phonenum
            user.nickname = phonenum
            user.save()

        request.session['uid'] = user.id

        data = {
            'code':0,
            'user':{
                'id': user.id,
                'nickname': user.nickname,
                'phonenum': user.phonenum,
                'birthday': user.birthday,
                'gender': user.gender,
                'location': user.location,
                'avatar': user.avatar
            }
        }
        return JsonResponse(data=data)

        

def show(request):
    '''查看个⼈、交友资料'''
    uid = request.session.get('uid')
    user = User.objects.get(pk=uid)
    data = {
        'code': 0,
        'data': {
            'dating_gender':user.dating_gender,
            'dating_location':user.dating_location,
            'max_distance':user.max_distance,
            'min_distance':user.min_distance,
            'max_dating_age':user.max_dating_age,
            'min_dating_age':user.min_dating_age,
            'vibration':user.vibration,
            'only_matched':user.only_matched,
            'auto_play':user.auto_play
        }
    }
    return JsonResponse(data=data)

def update(request):
    ''' 修改 个⼈资料 及 交友资料'''
    nickname = request.POST.get('nickname')
    birthday = request.POST.get('birthday')
    gender = request.POST.get('gender')
    location = request.POST.get('location')
    dating_gender = request.POST.get('dating_gender')
    dating_location = request.POST.get('dating_location')
    max_distance = request.POST.get('max_distance')
    min_distance = request.POST.get('min_distance')
    max_dating_age = request.POST.get('max_dating_age')
    min_dating_age = request.POST.get('min_dating_age')
    vibration = request.POST.get('vibration')
    only_matched = request.POST.get('only_matched')
    auto_play = request.POST.get('auto_play')

    uid = request.session.get('uid')
    user = User.objects.get(pk=uid)
    user.nickname = nickname
    user.birthday = birthday
    user.gender = gender
    user.location = location
    user.dating_gender = dating_gender
    user.dating_location = dating_location
    user.max_distance = max_distance
    user.min_distance = min_distance
    user.max_dating_age = max_dating_age
    user.min_dating_age = min_dating_age
    user.vibration = vibration
    user.only_matched = only_matched
    user.auto_play = auto_play
    user.save()
    return redirect('api/user/profile/show/')

