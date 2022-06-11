from rest_framework import serializers
from api.models import AccountInfo, CustomerInfo


class AccountInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountInfo
        fields = '__all__'


class CustomerInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerInfo
        fields = ['id','name','email','phone_number','date_of_birth','date_created']