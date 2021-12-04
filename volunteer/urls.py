from django.urls import path
from . import views

app_name = 'volunteer'

urlpatterns = [

    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
]
