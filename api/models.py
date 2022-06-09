from django.db import models
from django.utils import timezone


# Create your models here.

class CustomerInfo(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        db_table = "Customer_Info"


    def __str__(self):
        return self.name

class AccountInfo(models.Model):
    account_number = models.CharField(max_length=20)
    opening_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, null=True)


    class Meta:
        db_table = "Account_Info"

    def __str__(self):
        return self.account_number
    



    
