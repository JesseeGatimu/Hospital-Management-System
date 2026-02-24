from django.db import models

class Patient(models.Model):
    GENDER_CHOICES=(
        ('male','Male'),
        ('female','Female'),
    )
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
    age=models.IntegerField()
    phone=models.CharField(max_length=10)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# Create your models here.
