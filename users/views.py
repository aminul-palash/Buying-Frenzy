from rest_framework.generics import RetrieveAPIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, PurchaseHistorySerializer
from .models import Purchase_History, User

class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class PurchaseHistoryList(generics.ListCreateAPIView):
    queryset = Purchase_History.objects.all()
    serializer_class = PurchaseHistorySerializer

class PurchaseHistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase_History.objects.all()
    serializer_class = PurchaseHistorySerializer
    