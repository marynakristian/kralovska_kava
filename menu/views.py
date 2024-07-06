from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Coffee, Review
from .forms import ReservationForm, ReviewForm
from datetime import datetime


def home(request):
    form = ReviewForm()
    # Выбираем последние 4 отзыва, отсортированные по дате создания
    reviews = Review.objects.all().order_by('-review_date')[:4]
    return render(request, 'menu/home.html', {'form': form, 'reviews': reviews})

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            else:
                return redirect('home')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    return redirect('home')

def review_list(request):
    reviews = Review.objects.all().order_by('-id')[:4]
    context = {'reviews': reviews}
    return render(request, 'menu/review_list.html', context)

def coffee_list(request):
    coffees = Coffee.objects.all()
    return render(request, 'menu/coffee_list.html', {'coffees': coffees})

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