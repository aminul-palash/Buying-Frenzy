from django.urls import path
from .views import RestaurantList, RestaurantByDateTimeList
from .views import MenuDetail,MenuList
from .views import TopRestaurantsView, RestaurantSearchView

urlpatterns = [
    
    # assigned API ULR
    path('restaurants/bydatetime/', RestaurantByDateTimeList.as_view(), name='restaurant-bydatetime-list'),
    path('top-restaurants/', TopRestaurantsView.as_view(), name='restaurants-top'),
    path('restaurants/search/', RestaurantSearchView.as_view(), name='restaurant-search'),
    
    # ADDITIONAL API ULR
    path('restaurants/', RestaurantList.as_view(), name='restaurant-list'),
    path('menus/', MenuList.as_view(), name='menu-list'),
    path('menus/<int:pk>/', MenuDetail.as_view(), name='menu-detail'),
]