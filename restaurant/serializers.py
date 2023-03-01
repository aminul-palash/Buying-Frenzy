from rest_framework import serializers
from .models import Restaurant, Menu, OpeningHours

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'restaurant', 'dish_name', 'price')

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = ('id', 'restaurant', 'day_of_week', 'start_time', 'end_time')

class RestaurantSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True, read_only=True)
    opening_hours = OpeningHoursSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'cash_balance', 'menus', 'opening_hours')
