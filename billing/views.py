from django.shortcuts import render,redirect,get_object_or_404
from decimal import Decimal
from .models import Payment,Invoice
from patients.models import Patient

def invoice_list(request):
    invoices=Invoice.objects.all()
    return render(request,'billing\invoice_list.html',{'invoices':invoices})

def create_invoice(request):
    patients=Patient.objects.all()
    if request.method=='POST':
        Invoice.objects.create(
            patient_id=request.POST['patients'],
            total_amount=request.POST['total_amount'],
            amount_paid=0
        )
        return redirect('invoice_list')
    return render(request,'billing\create_invoice.html',{'patients':patients})

# Create your views here.
def make_payment(request,invoice_id):
    invoice=get_object_or_404(Invoice,id=invoice_id)
    if request.method=='POST':
        amount=Decimal(request.POST['amount'])
        Payment.objects.create(
            amount=amount,
            invoice=invoice,
            method=request.POST['method']
        )
        invoice.amount_paid+=amount
        if invoice.amount_paid==invoice.total_amount:
            invoice.status='paid'
        elif invoice.amount_paid>0:
            invoice.status='partial'

        invoice.save()
        return redirect('invoice_list')

    return render(request,'billing\make_payment.html',{'invoice':invoice})