from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PurchaseHistory
from .serializers import PurchaseHistorySerializer

class PurchaseHistoryList(generics.ListCreateAPIView):
    serializer_class = PurchaseHistorySerializer

    def get_queryset(self):
        food_name = self.request.query_params.get('dish_name', '')
        queryset = PurchaseHistory.objects.filter(user=self.request.user)
        if food_name:
            queryset = queryset.filter(dish_name__icontains=food_name)
        
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        
        if min_price is not None and max_price is not None:
            queryset = queryset.filter(transaction_amount__gte=min_price, transaction_amount__lte=max_price)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PurchaseHistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer



