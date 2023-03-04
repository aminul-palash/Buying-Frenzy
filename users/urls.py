from django.urls import path
from .views import PurchaseHistoryList, PurchaseHistoryDetail,CustomerList,CustomerDetail

urlpatterns = [
    path('', CustomerList.as_view(), name='users-list'),
    # path('users/<int:pk>/', CustomerDetail.as_view(), name='user-detail'),
    # path('purchase_history/', PurchaseHistoryList.as_view(), name='purchase_history_list'),
    # path('purchase_history/<int:pk>/', PurchaseHistoryDetail.as_view(), name='purchase_history_detail'),
]