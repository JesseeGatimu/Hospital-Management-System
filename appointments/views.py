from django.shortcuts import render,redirect
from .models import Appointments
from patients.models import Patient
from accounts.models import CustomUser
def appointment_list(request):
    appointments=Appointments.objects.all()
    return render(request,'appointments/appointment_list.html',{'appointments':appointments})

def add_appointments(request):
    patients=Patient.objects.all()
    doctor=CustomUser.objects.filter(role='doctor')
    if request.method=='POST':
        Appointment.objects.create(
            patient_id=request.POST['patient'],
            doctor_id=request.POST['doctor'],
            date=request.POST['date'],
            status=request.POST['status'],
            notes=request.POST['notes'],
        )
        return redirect('appointment_list')
    return render(request,'appointments/add_appointments.html',{
        'patients':patients,
        'doctors':patients
    })

# Create your views here.
