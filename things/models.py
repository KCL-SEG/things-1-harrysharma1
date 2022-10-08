from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser

class Thing(AbstractUser):
    name =models.CharField(unique=True, blank=True,max_length=30)
    description= models.TextField(blank=False, max_length=120)
    quantity=models.IntegerField()
    