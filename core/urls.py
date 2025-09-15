from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('tracks', views.trackspage, name='tracks'),
    path('checkout/<str:pk>/', views.checkoutPage, name='checkout'),
    path('track/<str:pk>/', views.trackpage, name='track'),
    path('events', views.eventspage, name='events'),
    path('event/<str:pk>/', views.eventpage, name='event'),
    path('signup',views.registrationpage, name='register'),
    path('login',views.UserLogin, name='login'),
    path('logout',views.UserLogout, name='logout'),
]
