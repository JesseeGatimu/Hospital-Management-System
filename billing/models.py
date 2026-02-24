from django.db import models
from patients.models import Patient

class Invoice(models.Model):
    STATUS_CHOICES=(
        ('paid','Paid'),
        ('unpaid','Unpaid'),
        ('partial','Partial'),
    )
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    amount_paid=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='unpaid')

    def balance(self):
        return self.total_amount-self.amount_paid

    def __str__(self):
        return f'Invoice :: {self.id} {self.patient}'

class Payment(models.Model):
    PAYMENT_METHODS=(
        ('mpesa','MPESA'),
        ('card','Card'),
        ('cash','Cash'),
    )
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    method=models.CharField(max_length=20,choices=PAYMENT_METHODS)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.amount} {self.method}'


# Create your models here.
