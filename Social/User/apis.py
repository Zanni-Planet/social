from urllib import request

from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def fetch_vcode(request):
    '''给用户发送验证码'''
    # 在request报文里面存放着前端页面传过来的数据，GET，POST是前端传过来的类字典对象，
    # get是方法，方法总共有九种
    phonenum=request.GET.get('phonenum')

    return JsonResponse()


def submit_vcode(request):
    return JsonResponse()


def show_profile(request):
    return JsonResponse()


def update_profile(request):
    return JsonResponse()


def qn_token(request):
    return JsonResponse()


def qn_callback(request):
    return JsonResponse()


def send_sms(request):
    return JsonResponse()
