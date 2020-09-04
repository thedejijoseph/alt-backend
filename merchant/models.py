from django.db import models
from django.contrib.auth.models import User

# from djongo import models

class Merchant(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, default='Nigeria')
