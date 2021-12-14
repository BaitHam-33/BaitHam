from django.shortcuts import render, redirect
from .models import event
from .forms import EventForm


def createEvent(request):
    """the function creat a new event according to the request of the user(admin only) and save it in the database"""
    if request.method == 'GET':
        return render(request, 'Event/createEvent.html', {'form': EventForm()})
    else:
        form = EventForm(request.POST)  # creat a form for the event
        new_event = form.save(commit=False)
        new_event.save()  # saving the new event in the database
        return redirect('Event:all_events')  # refers to the page of all events


def all_events(request):
    """""the function presents all events"""
    events = event.objects.order_by('-date')
    return render(request, 'Event/all_events.html', {'events': events})


def deleteEvent(request, event_id):
    """the function delete a event according to the request of the user (admin only) and delete it
         from the database """
    Event = event.objects.get(pk=event_id)
    Event.delete() # delete the report from the database
    return redirect('Event:all_events') # refers to the page of all events

def Event_detail(request, id=None):
    """the function presents a single page of each event according to the user request"""
    event_obj = None
    if id is not None:
        event_obj = event.objects.get(id=id)
    context = {"object": event_obj}
    return render(request, 'Event/event_detail.html', context=context)