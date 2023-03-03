from django.urls import path
from .views import RestaurantList, RestaurantDetail, RestaurantByDateTimeList,MenuDetail,MenuList,OpeningHoursDetail,OpeningHoursList,TopRestaurantsView


urlpatterns = [
    path('restaurants/', RestaurantList.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),
    # http://localhost:8000/api/restaurants/bydatetime/?date=2023-03-06&time=18:00:00
    path('restaurants/bydatetime/', RestaurantByDateTimeList.as_view(), name='restaurant-bydatetime-list'),
    path('top-restaurants/', TopRestaurantsView.as_view(), name='restaurants-top'),
    # /top-restaurants/?more_than=10&less_than=50&min_price=10&max_price=30&y=5
    path('menus/', MenuList.as_view(), name='menu-list'),
    path('menus/<int:pk>/', MenuDetail.as_view(), name='menu-detail'),
    path('opening_hours/', OpeningHoursList.as_view(), name='opening-hours-list'),
    path('opening_hours/<int:pk>/', OpeningHoursDetail.as_view(), name='opening-hours-detail'),
]