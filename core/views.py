from django.shortcuts import render, redirect
from .models import *
from .modelform import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    context = {}
    return render(request, 'core/homepage.html', context)

def checkoutPage(request, pk):
    event = eventModel.objects.get(id=pk)
    context = {'events':event}
    return render(request, 'core/checkout.html', context)

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
    page = 'register'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully. Please login now.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    context = {'form': form, 'page':page}
    return render(request, 'core/login-register.html', context)

def UserLogin(request):
    if request.user.is_authenticated:
        previous_page = request.META.get('HTTP_REFERER', '/')
        return redirect(previous_page)
    else:
        page = 'login'
        context = {'page':page}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
        
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, 'Username or Passward does not exist or matched')
        return render(request, 'core/login-register.html', context)

def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')