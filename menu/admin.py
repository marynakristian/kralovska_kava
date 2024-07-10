from django.contrib import admin
from .models import Coffee, Reservation, Review, Snack

admin.site.register(Review)

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'origin', 'roast_level')

class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'ingredients')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'number_of_people')
    search_fields = ('name', 'email', 'phone')



admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Snack, SnackAdmin)