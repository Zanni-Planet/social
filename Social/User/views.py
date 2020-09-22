from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from User.models import User

# Create your views here.
def show(request):
    '''查看个⼈、交友资料'''

    #data = {
    #    'code':0,
    #    'data':{

    #    }
    #}
    #return JsonResponse(data=data)
    # return HttpResponse('123')
