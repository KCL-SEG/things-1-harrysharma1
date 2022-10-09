
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(AbstractUser):
    name =models.CharField(max_length=30,unique=True)
    description= models.TextField(max_length=120,unique=False,blank=False)
    quantity=models.IntegerField(
        unique=False,
        default=0,
        validators=[MaxValueValidator(100),MinValueValidator(0)]
    )
    username=models.CharField(blank=True, unique=True, max_length=1)
    password=models.CharField(blank=True, max_length=2)
    