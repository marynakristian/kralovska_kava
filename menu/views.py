from django.shortcuts import redirect, render
from .models import Review
from .forms import ReservationForm, ReviewForm
from datetime import datetime


def home(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReviewForm()
    
    reviews = Review.objects.all().order_by('-review_date')[:4] 

    return render(request, 'menu/home.html', {'form': form, 'reviews': reviews})

def review_list(request):
    reviews = Review.objects.all().order_by('-id')[:4]
    context = {'reviews': reviews}
    return render(request, 'menu/review_list.html', context)

def coffee_list(request):
    return render(request, 'menu/coffee_list.html')

def snack_list(request):
    return render(request, 'menu/snack_list.html')


def location(request):
    return render(request, 'menu/location.html')

from django.shortcuts import render, redirect
from .forms import ReservationForm

def reservations(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'menu/reservations.html', {'form': form})

def reservation_success(request):
    return render(request, 'menu/reservation_success.html')