from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES=(
        ('admin','Admin'),
        ('doctor','Doctor'),
        ('nurse','Nurse'),
        ('receptionist','Receptionist'),
        ('pharmacist','pharmacist'),
    )
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
# Create your models here.
