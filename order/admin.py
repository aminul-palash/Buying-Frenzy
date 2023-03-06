from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, PurchaseHistory


admin.site.register(Customer)

admin.site.register(PurchaseHistory)

