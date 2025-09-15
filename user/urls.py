from django.urls import path
from . import views

urlpatterns = [
    path('user/dashboard/<str:pk>/', views.dashboardpage, name='dashboard'),
]
