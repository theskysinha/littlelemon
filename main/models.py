from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null = False)
    menu_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name