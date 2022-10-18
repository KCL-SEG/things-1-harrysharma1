
from enum import unique
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name=models.CharField(max_length=30,blank=False,unique=True,null=True)
    description=models.CharField(max_length=120,blank=True,unique=False,null=True)
    quantity=models.IntegerField(
        unique=False,
        blank=False,
        validators=[MinValueValidator(0),MaxValueValidator(100)],
        null=True
    )
 

    