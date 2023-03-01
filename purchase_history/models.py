from django.db import models
from django.conf import settings

class PurchaseHistory(models.Model):
    dish_name = models.CharField(max_length=255)
    restaurant_name = models.CharField(max_length=255)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.dish_name} at {self.restaurant_name}'
