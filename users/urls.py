from django.urls import path
from .views import PurchaseHistoryList, PurchaseHistoryDetail,CustomerList,CustomerDetail,PurchaseView

urlpatterns = [
    path('', CustomerList.as_view(), name='users-list'),
    path('purchase/', PurchaseView.as_view(), name='transaction'),
    # path('users/<int:pk>/', CustomerDetail.as_view(), name='user-detail'),
    # path('purchase_history/', PurchaseHistoryList.as_view(), name='purchase_history_list'),
    # path('purchase_history/<int:pk>/', PurchaseHistoryDetail.as_view(), name='purchase_history_detail'),
]

# curl --location --request POST 'http://localhost:8000/api/purchase/' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "username": "john_doe",
#     "restaurant_name": "McDonald's",
#     "menu_item_name": "Big Mac"
# }'

# {
#      "username": "Edith Johnson",
#    "restaurant_name": "3 Way Restaurant",
#     "menu_item_name": "Glackner Cigars"
# }


# curl -X POST -H "Content-Type: application/json" -d '{
#   "username": "myuser",
#   "restaurant_name": "myrestaurant",
#   "menu_item_name": "myitem"
# }' http://example.com/api/purchase/

# curl -X POST -H "Content-Type: application/json" -d '{
#    "username": "Edith Johnson",
#    "restaurant_name": "3 Way Restaurant",
#    "menu_item_name": "Glackner Cigars"
# }' http://localhost:8000/api/purchase/