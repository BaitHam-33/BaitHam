from django.shortcuts import render, redirect
from .models import event
from .forms import EventForm

def createEvent(request):
    if request.method == 'GET':
        return render(request, 'Report/createEvent.html', {'form': EventForm()})
    else:
        form = EventForm(request.POST)
        new_event = form.save(commit=False)
        new_event.save()
        return redirect('Event:all_events')


def all_events(request):
    events = event.objects.order_by('-date')
    return render(request, 'Event/all_events.html', {'events': events})


def deleteEvent(request, event_id):
    Event = event.objects.get(pk=event_id)
    Event.delete()
    return redirect('Event:all_events')
