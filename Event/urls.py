from django.urls import path
from . import views

app_name = 'Event'

urlpatterns = [
    path('all_events/', views.all_events, name='all_events'),
    path('createEvent/', views.createEvent, name='createEvent'),
    path('deleteEvent/<event_id>',views.deleteEvent,name='deleteEvent'),
]
