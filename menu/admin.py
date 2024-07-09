from django.contrib import admin
from .models import Coffee, Reservation, Review, Snack

admin.site.register(Review)

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'origin', 'roast_level')

class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'ingredients')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'number_of_people')
    list_filter = ('date', 'time')
    search_fields = ('name', 'email', 'phone')

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Snack, SnackAdmin)