from django.urls import path
from User import views

urlpatterns = [
    path('vcode/fetch', views.fetch, name='fetch'),
    path('vcode/submit', views.login, name='login'),
    path('profile/show/', views.show, name='show'),
    path('profile/update', views.update, name='update'),
]
