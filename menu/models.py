from django.db import models
from django.utils import timezone


    
class Review(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(null=True, blank=True)  # Сделали поле необязательным
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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField()
    image = models.ImageField(upload_to='snacks/')

    def __str__(self):
        return self.name

class Dessert(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField()
    image = models.ImageField(upload_to='desserts/')

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"