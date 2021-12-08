from django.urls import path
from . import views

app_name = 'volunteer'

urlpatterns = [
    #path('homeVolunteer',views.homeVolunteer,name='homeVolunteer'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
]
