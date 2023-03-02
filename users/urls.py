from django.urls import path
from .views import UserDetailAPIView
from .views import PurchaseHistoryList, PurchaseHistoryDetail

urlpatterns = [
    path('', UserDetailAPIView.as_view()),
    path('purchase_history/', PurchaseHistoryList.as_view(), name='purchase_history_list'),
    path('purchase_history/<int:pk>/', PurchaseHistoryDetail.as_view(), name='purchase_history_detail'),
]
