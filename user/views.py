from django.shortcuts import render

# Create your views here.
def dashboardpage(request):
    return render(request, 'user/dashboard.html')