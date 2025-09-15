from django.shortcuts import render
from core.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def dashboardpage(request, pk):
    return render(request, 'user/dashboard.html')