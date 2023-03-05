from rest_framework import generics
from .models import Restaurant, Menu, OpeningHours
from .serializers import RestaurantSerializer, MenuSerializer, OpeningHoursSerializer
from django.http import Http404
from rest_framework import status
import datetime
from django.db.models import Q,Count
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurant, OpeningHours, Menu
from rest_framework.filters import SearchFilter
from .serializers import RestaurantSerializer, OpeningHoursSerializer,MenuSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


class CustomPagination(PageNumberPagination):
    # http://example.com/api/restaurants/?p=2
    page_size = 10
    page_query_param = 'p'
    max_page_size = 100

class RestaurantSearchView(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'menus__dish_name']
    pagination_class = CustomPagination

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        queryset = Restaurant.objects.filter(
            Q(name__icontains=query) | Q(menus__dish_name__icontains=query)
        ).distinct().order_by('name')
        return queryset


class RestaurantByDateTimeList(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        date = self.request.query_params.get('date')
        time = self.request.query_params.get('time')

        if date is not None and time is not None:
            dt = datetime.datetime.strptime(date + " " + time, '%Y-%m-%d %H:%M:%S')
            weekday = dt.weekday()
            time = dt.time()

            queryset = queryset.filter(
                opening_hours__day_of_week=weekday, 
                opening_hours__start_time__lte=time, 
                opening_hours__end_time__gte=time
            )
        
        return queryset


class TopRestaurantsView(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        # Get query parameters
        more_than = self.request.query_params.get('more_than')
        less_than = self.request.query_params.get('less_than')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
       
        query = Restaurant.objects.annotate( num_dishes=Count('menus')).filter(
            num_dishes__gt=more_than,
            num_dishes__lt=less_than,
            # menus__price__gte=min_price ,
            # menus__price__lte=max_price,
        ).order_by('name')

        # Limit query to top y restaurants
        y = int(self.request.query_params.get('y', 10))
        query = query[:y]

        return query


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    pagination_class = CustomPagination
    

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = CustomPagination

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

