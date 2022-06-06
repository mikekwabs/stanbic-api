from django.urls import path,include
from . import views

urlpatterns = [
    path('add-customer/',views.AddNewCustomerAPI.as_view(), name="add" ),
    path('get-customers/',views.RetrieveAllCustomersAPI.as_view(), name="retreive_customers" ),
]
