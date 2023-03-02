from django.core.management.base import BaseCommand
import json
from users.models import User, Purchase_History
from restaurant.models import Restaurant, Menu

class Command(BaseCommand):
    help = 'Import user data'

    def add_arguments(self, parser):
        parser.add_argument('--app', type=str)
        parser.add_argument('--data', type=str)

    def handle(self, *args, **options):
        app_name = options['app']
        data_str = options['data']

        print(app_name)
        print(data_str)

        # Parse the JSON data
        user_data = json.loads(data_str)

        # Set the default password
        default_password = 'mypassword'

        # Create User objects from the data and save to database
        for user in user_data["users"]:
           
            try:
                u = User.objects.create(username=user['name'], cash_balance=user['cash_balance'])
                u.set_password(default_password)
                u.save()
            except KeyError as e:
                print(f"Error creating user: {e}")
                continue
            for purchase in user['purchase_history']:
                try:
                    # Retrieve restaurant based on its name in the purchase history
                    restaurant = Restaurant.objects.get(name=purchase['restaurant_name'])
                    # Retrieve menu item based on its name and restaurant_id
                    menu_item = Menu.objects.get(dish_name=purchase['dish_name'], restaurant_id=restaurant.id)
                    # Create PurchaseHistory object and save to database
                    Purchase_History.objects.create(user=u, restaurant=restaurant, menu=menu_item, transaction_amount=purchase['transaction_amount'], transaction_date=purchase['transaction_date'])
                except (KeyError, Restaurant.DoesNotExist, Menu.DoesNotExist) as e:
                    print(f"Error creating purchase history for user {u.username}: {e}")
                    continue
        