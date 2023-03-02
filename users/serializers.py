from rest_framework import serializers
from .models import User, Purchase_History

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'cash_balance']
        extra_kwargs = {'password': {'write_only': True}}


class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_History
        fields = ('id', 'user', 'restaurant', 'menu', 'transaction_amount', 'transaction_date')
