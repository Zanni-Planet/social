from django.urls import path
from User import views

urlpatterns = [
    path('profile/show/',views.show,name='show')
]
