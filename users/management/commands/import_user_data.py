from django.core.management.base import BaseCommand
import json,datetime
from django.utils import timezone
from users.models import Customer, PurchaseHistory
from restaurant.models import Restaurant, Menu

class Command(BaseCommand):
    help = 'Import user data'

    def add_arguments(self, parser):
        parser.add_argument('--app', type=str)
        parser.add_argument('--data', type=str)

    def handle(self, *args, **options):
        app_name = options['app']
        data_str = options['data']

        # Parse the JSON data
        user_data = json.loads(data_str)

        # Create User objects from the data and save to database
        for user in user_data:
            try:
                u = Customer.objects.get(name=user['name'])
                u.cash_balance = user['cashBalance']
                u.save()
            except Customer.DoesNotExist:
                u = Customer.objects.create(name=user['name'], cash_balance=user['cashBalance'])
                u.save()
           
            for purchase in user['purchaseHistory']:
                try:
                    # Retrieve or create Restaurant object based on its name
                    restaurant, created = Restaurant.objects.get_or_create(name=purchase['restaurantName'])
                    # Retrieve or create Menu object based on its name and restaurant
                    menu_item, created = Menu.objects.get_or_create(dish_name=purchase['dishName'],price = purchase["transactionAmount"], restaurant=restaurant)
                    try:
                        purchase['transactionDate'] = datetime.datetime.strptime(purchase['transactionDate'], "%Y-%m-%d %H:%M")
                        transaction_date = timezone.make_aware(purchase['transactionDate'], timezone.get_default_timezone())
                    
                    except ValueError:
                        # The datetime string is invalid, set a default date
                        # handling invalid date
                        transaction_date = datetime.datetime(2020, 1, 1)
                        transaction_date = timezone.make_aware(transaction_date, timezone.get_default_timezone())

                    PurchaseHistory.objects.create(user=u, restaurant=restaurant, menu=menu_item, transaction_amount=purchase['transactionAmount'], transaction_date=transaction_date)
                
                except (KeyError, Restaurant.DoesNotExist, Menu.DoesNotExist) as e:
                    print(f"Error creating purchase history for user {u.name}: {e}")
                    continue
        