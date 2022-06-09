from django.urls import path
from . import views

urlpatterns = [
    path('add-customer/',views.AddNewCustomerAPI.as_view(), name="add" ),
    path('get-customers/',views.RetrieveAllCustomersAPI.as_view(), name="retrieve_custom"),
    path('get-customer-phone/<str:pk>',views.RetrieveByPhoneAPI.as_view(), name="get_customers" ),
    path('update-customer/<int:pk>',views.UpdateCustomerInfoAPI.as_view(), name="update_customers" ),
    path('add-account/',views.AddNewAccountAPI.as_view(), name="add_customers" ),
    path('get-accounts-phone/<str:pk>',views.RetrieveAccountsByPhone.as_view(), name="get_accounts" ),

]






