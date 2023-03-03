from rest_framework.generics import RetrieveAPIView
from rest_framework import generics
from .serializers import UserSerializer, PurchaseHistorySerializer
from .models import PurchaseHistory, Customer
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    # http://example.com/api/restaurants/?p=2
    page_size = 10
    page_query_param = 'p'
    max_page_size = 100

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer
    

class PurchaseHistoryList(generics.ListCreateAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
    pagination_class = CustomPagination

class PurchaseHistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
    