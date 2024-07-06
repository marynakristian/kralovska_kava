from django.db import models
from django.utils import timezone


    
class Review(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='coffees/')
    origin = models.CharField(max_length=100, blank=True, null=True)
    roast_level = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Snack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='desserts/')
    ingredients = models.CharField(max_length=255, blank=True, null=True)  # Ингредиенты

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"