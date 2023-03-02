from rest_framework import serializers
from .models import User, Purchase_History

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(default='dummy_password')
    class Meta:
        model = User
        fields = ['id', 'username', 'cash_balance','password']
        read_only_fields = ['id']
        


class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_History
        fields = ('id', 'user', 'restaurant', 'menu', 'transaction_amount', 'transaction_date')
