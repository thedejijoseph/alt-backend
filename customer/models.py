from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# experiment is to find out where user data is stored

class Customer(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, default='')

