from django import forms
from .models import Reservation, Review

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'number_of_people']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'name': 'Jméno',
            'email': 'E-mail',
            'phone': 'Telefon',
            'date': 'Datum',
            'time': 'Čas',
            'number_of_people': 'Počet osob',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'comment']