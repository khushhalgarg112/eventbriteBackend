from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Ignore this Person Model this is created to test the Django Api
class Person(AbstractUser):
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email


class Auth(models.Model):
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email

class Event(models.Model):
    title = models.CharField(max_length = 100)
    summary = models.CharField(max_length=1000)
    date = models.DateField()
    time = models.TimeField(default = "12:00:00")
    location = models.CharField(max_length = 60)
    image = models.CharField(default="", max_length = 2000)
    is_liked = models.BooleanField(default = False)
    user = models.EmailField(max_length=60)

    def __str__(self):
        return self.email

# Like model to store the liked post of each user with the event id
class Like(models.Model):
    like = models.BooleanField(default = False)
    user = models.EmailField(max_length=60)
    eventid = models.IntegerField()