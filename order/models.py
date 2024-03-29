from django.db import models
from django.conf import settings
from restaurant.models import Restaurant, Menu

from django.contrib.auth.models import User


 

class Customer(models.Model):
    name = models.CharField(max_length=255)
    cash_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class PurchaseHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.user.name} bought {self.menu.dish_name} for {self.transaction_amount} at {self.restaurant.name} on {self.transaction_date}"

class Payment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username


class Transaction(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username