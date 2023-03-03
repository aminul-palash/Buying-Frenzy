from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, PurchaseHistory

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'cash_balance', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'cash_balance')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'cash_balance', 'is_staff', 'is_active')
        }),
    )

admin.site.register(User, CustomUserAdmin)

admin.site.register(PurchaseHistory)

