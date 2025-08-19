from django.shortcuts import render
from .models import *
from .modelform import userform

# Create your views here.
def homepage(request):
    form = userform()
    context = {'form':form}
    return render(request, 'core/homepage.html', context)

def trackspage(request):
    track = trackModel.objects.all()
    context = {"tracks":track}
    return render(request, 'core/tracks.html', context)

def trackpage(request,pk):
    track = trackModel.objects.get(id=pk)
    booking = bookingModel.objects.filter(booking_track = track)
    context = {'tracks':track, 'booking':booking}
    return render(request, 'core/track.html', context)

def eventspage(request):
    event = eventModel.objects.all()
    context = {'events':event}
    return render(request, 'core/events.html', context)

def eventpage(request,pk):
    event = eventModel.objects.get(id=pk)
    context = {'events':event}
    return render(request, 'core/event.html', context)

def registrationpage(request):
    # if request.method == 'POST':
    #     first = request.POST['first']
    #     last = request.POST['last']
    #     username = request.POST['username']
    #     email = request.POST['mail']
    #     password = request.POST['password']

    return render(request, 'core/login-register.html')