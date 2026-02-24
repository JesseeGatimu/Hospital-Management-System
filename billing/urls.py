from django.urls import path 
from . import views

urlpatterns=[
    path('',views.invoice_list,name="invoice_list"),
    path('create/',views.create_invoice,name="create_invoice"),
    path('pay/<int:invoice_id>',views.make_payment,name="make_payment"),
]