from enum import unique
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

class Thing(AbstractUser):
    name =models.CharField(max_length=30)
    description= models.TextField()
    quantity=models.IntegerField()
    username=models.CharField(blank=True, unique=True, max_length=1)
    password=models.CharField(blank=True, max_length=2)
    