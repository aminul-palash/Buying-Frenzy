from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, PurchaseHistory, Payment, Transaction


admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Transaction)

admin.site.register(PurchaseHistory)

