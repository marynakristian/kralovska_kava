from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservationViewSet

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet)


urlpatterns = [
    
    path('', views.home, name='home'),
    path('coffees/', views.coffee_list, name='coffee_list'),
    path('snacks/', views.snack_list, name='snack_list'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('location/', views.location, name='location'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('api/', include(router.urls)),

]