from django import forms
from .models import  Reservation, Review


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

        # Add your validation logic here (e.g., checking for availability)
        if Reservation.objects.filter(date=date, time=time).count() >= 10:  # Example: no more than 10 reservations at the same time
            raise forms.ValidationError("Na vybraný čas jsou všechna místa již obsazena.")
        
        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'comment']