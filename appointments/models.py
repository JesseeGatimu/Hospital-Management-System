from django.db import models
from patients.models import Patient
from accounts.models import CustomUser

class Appointments(models.Model):
    STATUS_CHOICES=(
        ('pending','Pending'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    )
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date=models.DateTimeField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    notes=models.TextField()

    def __str__(self):
        return f"{self.patient} - {self.doctor} {self.date}"
# Create your models here.
