
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import CustomerInfo,AccountInfo
from api.serializers import AccountInfoSerializer,CustomerInfoSerializer



# Create your views here.

#Add a new customer
class AddNewCustomerAPI(generics.CreateAPIView):
    serializer_class = CustomerInfoSerializer

    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.save()
        return Response({
            'customer': CustomerInfoSerializer(customer,context=self.get_serializer_context()).data
        },status=status.HTTP_201_CREATED)

#Retrieve all customers 
class RetrieveAllCustomersAPI(generics.GenericAPIView):
    serializer_class = CustomerInfoSerializer
        
    def get_queryset(self):
        return CustomerInfo.objects.all()

    def get(self,request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            serializer = CustomerInfoSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            content = {'Sorry. Nothing in the database.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


# Update Customer info
class UpdateCustomerInfoAPI(generics.GenericAPIView):
    serializer_class = CustomerInfoSerializer

    def put(self,request ,pk,*args, **kwargs):
        try:
            customer_info = CustomerInfo.objects.get(pk=pk)
        except CustomerInfo.DoesNotExist:
            return Response({'message': "Query does not exist."},status=status.HTTP_404_NOT_FOUND)
        
        serializer = CustomerInfoSerializer(customer_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
#Retrieve a customer’s info by phone number
class RetrieveByPhoneAPI(generics.GenericAPIView):
    serializer_class = CustomerInfoSerializer
    lookup_field = 'pk'

    def get(self, request,*args, **kwargs):
        phone = kwargs['pk']
        try:
            queryset = CustomerInfo.objects.get(phone_number=phone)
        except CustomerInfo.DoesNotExist:
            return Response({'message': 'Query does not exist.'},status=status.HTTP_404_NOT_FOUND)
        
        if queryset:
            serializer = CustomerInfoSerializer(queryset)
            return Response(serializer.data)



#Retrieve a customer’s info by email number
class RetrieveByEmailAPI(generics.GenericAPIView):
    serializer_class = CustomerInfoSerializer
    lookup_field = 'pk'
    lookup_value_regex = "[^\]]+"

    def get(self, request,*args, **kwargs):
        mail = kwargs['pk']
        queryset = CustomerInfo.objects.get(email=mail)
        if queryset:
            serializer = CustomerInfoSerializer(queryset)
            return Response(serializer.data)
        else:
            content = {'Data not found.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


#Delete an account by account number
class DeleteByAccNumberAPI(generics.GenericAPIView):

    def delete(self, request, pk, format=None):
        queryset = AccountInfo.objects.all().filter(account_number=pk)
        if queryset.exists():
            queryset.delete()
            return Response({'message':'Deleted successfully.'})
        else:
            return Response({'message':'Data cannot be found.'},status=status.HTTP_404_NOT_FOUND)
    

class AddNewAccountAPI(generics.GenericAPIView):
    serializer_class = AccountInfoSerializer

    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            customer = CustomerInfo.objects.get(id=serializer.data['customer'])
            AccountInfo.objects.create(
                account_number = serializer.data["account_number"],
                opening_amount = serializer.data["opening_amount"],
                current_balance = serializer.data['current_balance'],
                date_created = serializer.data['date_created'],
                customer = customer
            
            ) 
            return Response({'message':'Account created successfully.'},status=status.HTTP_201_CREATED) 
        except AccountInfo.DoesNotExist:
            return Response({'message': 'Account is not found.'},status=status.HTTP_404_NOT_FOUND)
        
        

class RetrieveAccountsByPhoneAPI(APIView):
    serializer_class = AccountInfoSerializer

    def get(self, request, pk,*args, **kwargs):
        try:
            customer = CustomerInfo.objects.get(phone_number = pk)
            accounts = AccountInfo.objects.filter(customer = customer)
            serializer = AccountInfoSerializer(accounts, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except AccountInfo.DoesNotExist:
            return Response({'message': 'Account is not found.'},status=status.HTTP_404_NOT_FOUND)

            
class RetrieveAccountsByEmailAPI(APIView):
    serializer_class = AccountInfoSerializer

    def get(self, request,pk,*args, **kwargs):
        try:
            customer = CustomerInfo.objects.get(email = pk)
            accounts = AccountInfo.objects.filter(customer = customer)
            serializer = AccountInfoSerializer(accounts, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        except AccountInfo.DoesNotExist:
            return Response({'message': 'Account is not found.'},status=status.HTTP_404_NOT_FOUND)

            

class DeleteCustomerAndAllLinkedAccAPI(APIView):

    def delete(self, request, pk,*args, **kwargs):
        customer = CustomerInfo.objects.get(id = pk)
        accounts = AccountInfo.objects.all().filter(customer = customer)
        if customer and accounts:
            accounts.delete()
            customer.delete()
            return Response({'message':'Customer deleted successfully.'})
        else:
            return Response({'message':'Customer does not exist.'},status=status.HTTP_404_NOT_FOUND)



        
    


