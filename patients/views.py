from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient

def patient_list(request):
    patients=Patient.objects.all()
    return render(request, 'patients/patient_list.html',{'patients':patients})

def add_patient(request):
    if request.method=="POST":
        Patient.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            gender=request.POST['gender'],
            age=request.POST['age'],
            phone=request.POST['phone'],
            address=request.POST['address'],
        )
        return redirect('patient_list')
    
    return render(request, 'patients/add_patient.html')

def edit_patient(request,id):
    patient=get_object_or_404(Patient,id=id)

    if request.method=='POST':
        patient.first_name=request.POST['first_name']
        patient.last_name=request.POST['last_name']
        patient.gender=request.POST['gender']
        patient.age=request.POST['age']
        patient.phone=request.POST['phone']
        patient.address=request.POST['address']
        patient.save()
        return redirect('patient_list')
    return render(request,'patients/edit_patient.html',{'patient':patient})

def delete_patient(request,id):
    patient=get_object_or_404(Patient,id=id)
    patient.delete()
    return redirect('patient_list')
# Create your views here.
