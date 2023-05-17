from rest_framework import serializers
from .models import Customer, PurchaseHistory, Payment, Transaction
from rest_framework import serializers
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'cash_balance')
        

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = ('id', 'user', 'restaurant', 'menu', 'transaction_amount', 'transaction_date')



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class PaymentSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()

    class Meta:
        model = Payment
        fields = ('id', 'user', 'amount', 'timestamp')

class TransactionSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()
    payment = PaymentSerializer()

    class Meta:
        model = Transaction
        fields = ('id', 'user', 'payment', 'timestamp')
