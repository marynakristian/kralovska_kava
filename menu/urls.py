from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coffee_list/', views.coffee_list, name='coffee_list'),
    path('snack_list/', views.snack_list, name='snack_list'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('', views.home, name='home'),
    path('location/', views.location, name='location'),
]