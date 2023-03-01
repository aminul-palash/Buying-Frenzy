from django.urls import path
from .views import PurchaseHistoryList, PurchaseHistoryDetail

urlpatterns = [
    path('purchase_history/', PurchaseHistoryList.as_view(), name='purchase_history_list'),
    path('purchase_history/<int:pk>/', PurchaseHistoryDetail.as_view(), name='purchase_history_detail'),
]
