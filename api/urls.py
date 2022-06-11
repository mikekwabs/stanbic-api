from django.urls import path
from . import views

urlpatterns = [
    path('add-customer/',views.AddNewCustomerAPI.as_view(), name="add_customer" ),
    path('get-customers/',views.RetrieveAllCustomersAPI.as_view(), name="retrieve_customer"),
    path('get-customer-phone/<str:pk>',views.RetrieveByPhoneAPI.as_view(), name="get_customers" ),
    path('get-customer-mail/<str:pk>',views.RetrieveByEmailAPI.as_view(), name="get_customers" ),
    path('update-customer/<int:pk>',views.UpdateCustomerInfoAPI.as_view(), name="update_customer" ),
    path('add-account/',views.AddNewAccountAPI.as_view(), name="add_account" ),
    path('get-accounts-phone/<str:pk>',views.RetrieveAccountsByPhoneAPI.as_view(), name="get_accounts" ),
    path('get-accounts-mail/<str:pk>',views.RetrieveAccountsByEmailAPI.as_view(), name="get_accounts" ),
    path('delete-account/<int:pk>',views.DeleteByAccNumberAPI.as_view(), name="delete-account" ),
    path('delete-customer/<int:pk>',views.DeleteCustomerAndAllLinkedAccAPI.as_view(), name="delete-customer" ),

]




