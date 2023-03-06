from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    # ASSIGNED API URL
    path('api/', include('order.urls')), # Include users app URLs
    path('api/', include('restaurant.urls')), # Include purchase_history app URLs

    # ADDITIONAL API URL
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # Add Django REST Framework auth views
    
]