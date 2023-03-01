from django.urls import path
from .views import RestaurantList, RestaurantDetail, RestaurantByDateTimeList,MenuDetail,MenuList,OpeningHoursDetail,OpeningHoursList,TopRestaurantsView


urlpatterns = [
    path('restaurants/', RestaurantList.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),
    path('restaurants/bydatetime/', RestaurantByDateTimeList.as_view(), name='restaurant-bydatetime-list'),
    path('top-restaurants/', TopRestaurantsView.as_view(), name='restaurants-top'),
    
    path('menus/', MenuList.as_view(), name='menu-list'),
    path('menus/<int:pk>/', MenuDetail.as_view(), name='menu-detail'),
    path('opening_hours/', OpeningHoursList.as_view(), name='opening-hours-list'),
    path('opening_hours/<int:pk>/', OpeningHoursDetail.as_view(), name='opening-hours-detail'),
]