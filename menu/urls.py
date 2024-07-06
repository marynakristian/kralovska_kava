from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coffees/', views.coffee_list, name='coffee_list'),
    path('snack_list/', views.snack_list, name='snack_list'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('location/', views.location, name='location'),
    path('submit_review/', views.submit_review, name='submit_review'),   
]