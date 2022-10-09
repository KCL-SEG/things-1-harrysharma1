
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(AbstractUser):
    name =models.CharField(max_length=30,unique=True)
    description= models.CharField(max_length=120,blank=True)
    quantity=models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100),MinValueValidator(0)]
    )
    username=models.CharField(blank=True, unique=True, max_length=20)
    password=models.CharField(blank=True, max_length=20)
    