from django.urls import path
from .views import CustomerList,CustomerDetail,PurchaseView
from django.urls import path
from .views import UserRegistrationView, UserLoginView



urlpatterns = [
    
    # ASSIGNED API URL
    path('purchase/', PurchaseView.as_view(), name='transaction'),

    # ADDITIONAL API URL
    path('users/', CustomerList.as_view(), name='users-list'),
    path('users/<int:pk>/', CustomerDetail.as_view(), name='user-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]