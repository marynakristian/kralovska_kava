from django.contrib import admin
from .models import Coffee, Review, Snack

admin.site.register(Review)

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'origin', 'roast_level')

class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'ingredients')

admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Snack, SnackAdmin)