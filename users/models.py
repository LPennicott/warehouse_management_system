from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class CustomUser(AbstractUser):
    departments = [
        ('OE', 'Ocean Export'),
        ('OI', 'Ocean Import'),
        ('AE', 'Air Export'),
        ('AI', 'Air Import'),
        ('321', 'Section 321'),
        ('CC', 'Cargo City'),
    ]
    department = models.CharField(
        max_length=10,
        choices=departments,
    )


