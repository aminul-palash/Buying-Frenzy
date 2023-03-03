from django.db import models
import uuid
from django.utils import timezone


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    cash_balance = models.DecimalField(max_digits=8, decimal_places=2,default=0.0)

    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    dish_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2,default=0.0)

    def __str__(self):
        return self.dish_name


class OpeningHours(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='opening_hours')
    day_of_week = models.IntegerField(choices=zip(range(7), ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')))
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return f'{self.get_day_of_week_display()} {self.start_time} - {self.end_time}'




















# from django.db import models

# class Restaurant(models.Model):
#     name = models.CharField(max_length=255)
#     cash_balance = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.name

# class Menu(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
#     dish_name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.dish_name

# class OpeningHours(models.Model):
#     DAYS_OF_WEEK = (
#         (0, 'Mon'),
#         (1, 'Tue'),
#         (2, 'Wed'),
#         (3, 'Thu'),
#         (4, 'Fri'),
#         (5, 'Sat'),
#         (6, 'Sun')
#     )
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='opening_hours')
#     day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)
#     start_time = models.TimeField()
#     end_time = models.TimeField()

#     def __str__(self):
#         return self.day_of_week
    

# # models.py
# from django.db import models

# class Restaurant(models.Model):
#     name = models.CharField(max_length=255)
#     cash_balance = models.DecimalField(max_digits=8, decimal_places=2)

# class Menu(models.Model):
    
#     restaurant = models.ForeignKey(Restaurant, related_name='menu_items', on_delete=models.CASCADE)
#     dish_name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=6, decimal_places=2)


