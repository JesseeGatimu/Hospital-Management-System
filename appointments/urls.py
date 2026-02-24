from . import views
from django.urls import path
urlpatterns=[
    path('',views.appointment_list,name="appointment_list"),
    path('add/',views.add_appointments,name="add_appointments"),
]