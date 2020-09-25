from django.conf.urls import url

from User import sms, apis

urlpatterns=[
    url(r"^sms/", apis.sms, name=sms)
]