from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='users')

class CommercialUser(User):
    pass

class SpecialOffer(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='special_offers/', null=True)
    pricing = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    availability = models.BooleanField(default=True)
    terms_and_conditions = models.TextField(null=True)

    def __str__(self):
        return self.title

class Room(models.Model):
    name = models.CharField(max_length=255, null=False)
    capacity = models.IntegerField(null=False)
    amenities = models.TextField(null=True)
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    picture = models.ImageField(upload_to='rooms/', null=True)

    def __str__(self):
        return self.name
    
class Style(models.Model):
    name = models.CharField(max_length=255, null=False)
    capacity = models.IntegerField(null=False)
    amenities = models.TextField(null=True)
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    picture = models.ImageField(upload_to='styles/', null=True)

    def __str__(self):
        return self.name


class CoffeeBreak(models.Model):
    name = models.CharField(max_length=255, null=False)
    menu_items = models.TextField(null=True)
    pricing_per_person = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    serving_sizes = models.CharField(max_length=255, null=True)
    picture = models.ImageField(upload_to='coffee_breaks/', null=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=256, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    event_room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    event_style = models.ForeignKey(Style, on_delete=models.CASCADE, null=True, blank=True)
    coffee_break = models.ForeignKey(CoffeeBreak, on_delete=models.SET_NULL, null=True)
    date_and_time = models.DateTimeField(null=False)
    number_of_attendees = models.IntegerField(null=False)
    notes = models.TextField(blank=True, null=True)



    
    
def __str__(self):
    return f'{self.event_room} , {self.coffee_break} ,on {self.date_and_time}'


class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='favorites')
    special_offer = models.ForeignKey(SpecialOffer, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.special_offer


class Contact(models.Model):
    full_name = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=50,null=True)
    message = models.TextField(null=True)
    
    def __str__(self):
        return self.full_name


