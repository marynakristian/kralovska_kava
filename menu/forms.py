from django import forms
from .models import  Reservation, Review
from datetime import time as datetime_time



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'number_of_people']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }
        labels = {
            'name': 'Jmeno',
            'email': 'Email',
            'phone': 'Telefon',
            'date': 'Datum',
            'time': 'Čas',
            'number_of_people': 'Počet osob'
        }
        help_texts = {
            'date': 'Vyberte datum vaší rezervace.',
            'time': 'Vyberte čas vaší rezervace.'
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            # Валидация времени: разрешено только с 9 утра до 8 вечера
            if time < datetime_time(hour=9, minute=0):
                raise forms.ValidationError("Rezervace je možná pouze od 9:00.")
            elif time >= datetime_time(hour=20, minute=0):
                raise forms.ValidationError("Rezervace je možná pouze do 20:00.")

            # Проверка наличия бронирований на выбранное время
            reservations_count = Reservation.objects.filter(date=date, time=time).count()
            if reservations_count >= 10:
                raise forms.ValidationError("Na vybraný čas jsou všechna místa již obsazena.")

        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'comment']