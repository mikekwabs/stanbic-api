from multiprocessing import context
from rest_framework import generics
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
        })



class RetrieveAllCustomersAPI(generics.GenericAPIView):
    serializer_class = CustomerInfoSerializer

    def get(self,request, *args, **kwargs):
        customers = CustomerInfo.objects.all().order_by('id')
        return Response({
            "customers": self.serializer_class(customers,context={'request': request}, many=True).data
        })