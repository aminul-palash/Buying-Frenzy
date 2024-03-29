from rest_framework.generics import RetrieveAPIView
from rest_framework import generics
from .serializers import CustomerSerializer, PurchaseHistorySerializer
from .models import PurchaseHistory, Customer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PurchaseHistory, Restaurant, Customer
from .serializers import PurchaseHistorySerializer
from restaurant.models import Restaurant, Menu
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import UserRegistrationSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from .serializers import UserLoginSerializer

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if user exists
        try:
            user = User.objects.get(username=serializer.validated_data['username'])
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid credentials')

        # Check if password is correct
        if not user.check_password(serializer.validated_data['password']):
            raise AuthenticationFailed('Invalid credentials')

        # Generate access token
        access_token = AccessToken.for_user(user)

        return Response({'access_token': str(access_token)})


class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        access_token = AccessToken.for_user(user)
        return Response({'access_token': str(access_token)})



class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'
    max_page_size = 100


class PurchaseView(APIView):

    def post(self, request):
        # Get the request data
        username = request.data.get('username')
        restaurant_name = request.data.get('restaurant_name')
        menu_item_name = request.data.get('menu_item_name')

        # Get the user and check if they have enough cash balance
        user = get_object_or_404(Customer, name__iexact=username)
        # menu_item = get_object_or_404(Menu, dish_name__iexact=menu_item_name)
        # menu_item = Menu.objects.filter(dish_name__iexact=menu_item_name).first()
        menu_item = Menu.objects.filter(restaurant__name__iexact=restaurant_name, dish_name__iexact=menu_item_name).first()

        if menu_item is None:
            return Response({'error': 'Menu not found at specified restaurant'}, status=status.HTTP_404_NOT_FOUND)

        if user.cash_balance < menu_item.price:
            return Response({
                'message': 'Insufficient cash balance'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Calculate the transaction amount and update the user's cash balance
        transaction_amount = menu_item.price
        user.cash_balance -= transaction_amount
        

        # Retrieve the restaurant by name and create a new PurchaseHistory instance
        restaurant = get_object_or_404(Restaurant, name__iexact=restaurant_name)
        purchase = PurchaseHistory.objects.create(
            menu_id=menu_item.id,
            restaurant_id=restaurant.id,
            user_id=user.id,
            transaction_amount=transaction_amount,
            transaction_date=timezone.now()
        )

        # Update the cash balance of the restaurant
        restaurant.cash_balance += transaction_amount
        restaurant.save()
        user.save()

        # Return a response indicating success and the updated cash balances
        serializer = PurchaseHistorySerializer(purchase)
        return Response({
            'message': 'Purchase successful',
            'restaurant_cash_balance': restaurant.cash_balance,
            'user_cash_balance': user.cash_balance,
            'purchase': serializer.data
        }, status=status.HTTP_201_CREATED)


class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomPagination

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

