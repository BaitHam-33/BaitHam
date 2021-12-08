from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Donations'

urlpatterns = [

    path('new/', views.donates_from, name="new"),  # שולח לטופס
    path('submit', views.submit, name="submit"),  # שולח לדאטא בייס
    path('all_Donors', views.all_Donors, name="all_Donors")  # הצגת התורמים

]
