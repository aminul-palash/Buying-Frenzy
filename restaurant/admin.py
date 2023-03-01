from django.contrib import admin
from .models import Restaurant, Menu, OpeningHours

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(OpeningHours)
