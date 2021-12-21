from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Donations'

urlpatterns = [

    path('new/', views.donates_form, name="new"),  # שולח לטופס
    path('Thankyou/', views.Thankyou, name="Thankyou"),  # שולח לטופס
    path('submit', views.submit, name="submit"),  # שולח לדאטא בייס
    path('all_Donors', views.all_Donors, name="all_Donors"),  # הצגת התורמים
    path('export_pdf',views.export_pdf,name="export_pdf"),
    path('export_excel', views.export_excel, name="export_excel"),

]
