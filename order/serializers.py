from rest_framework import serializers
from .models import Customer, PurchaseHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'cash_balance')
        

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = ('id', 'user', 'restaurant', 'menu', 'transaction_amount', 'transaction_date')
