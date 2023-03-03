from rest_framework import generics
from .models import Restaurant, Menu, OpeningHours
from .serializers import RestaurantSerializer, MenuSerializer, OpeningHoursSerializer
from django.http import Http404
from rest_framework import status
from django.db.models import Q,Count
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurant, OpeningHours
from .serializers import RestaurantSerializer, OpeningHoursSerializer,MenuSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

class CustomPagination(PageNumberPagination):
    # http://example.com/api/restaurants/?p=2
    page_size = 10
    page_query_param = 'p'
    max_page_size = 100

class RestaurantByDateTimeList(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    pagination_class = CustomPagination
    def get_queryset(self):
        queryset = Restaurant.objects.all()
        dt = self.request.query_params.get('datetime')
        if dt is not None:
            dt = timezone.datetime.fromisoformat(dt)
            weekday = dt.weekday()
            time = dt.time()
            print(weekday)
            print(time)
            queryset = queryset.filter(opening_hours__day_of_week=weekday, opening_hours__start_time__lte=time, opening_hours__end_time__gte=time)
        return queryset
    
class TopRestaurantsView(APIView):
    def get(self, request, format=None):
        # Get query parameters
        num_dishes = request.query_params.get('num_dishes')
        price_min = request.query_params.get('price_min')
        price_max = request.query_params.get('price_max')
        top_restaurants = request.query_params.get('top_restaurants')
        less_than = request.query_params.get('less_than')

        # Filter restaurants by price range
        restaurants = Restaurant.objects.filter(menus__price__gte=price_min, menus__price__lte=price_max)
        print(restaurants)
        # Filter restaurants by number of dishes
        if num_dishes:
            if less_than:
                restaurants = restaurants.annotate(num_menu=Count('menus')).filter(num_menu__lt=num_dishes)
            else:
                restaurants = restaurants.annotate(num_menu=Count('menus')).filter(num_menu__gt=num_dishes)

        # Rank restaurants alphabetically
        restaurants = restaurants.order_by('name')

        # Get top y restaurants
        if top_restaurants:
            restaurants = restaurants[:int(top_restaurants)]

        # Serialize and return data
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)



class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    pagination_class = CustomPagination

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = CustomPagination

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OpeningHoursList(generics.ListCreateAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer
    pagination_class = CustomPagination

class OpeningHoursDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer


