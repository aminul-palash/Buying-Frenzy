from django.core.management.base import BaseCommand
import json,uuid
from restaurant.models import Restaurant, Menu, OpeningHours

class Command(BaseCommand):
    help = 'Import restaurant data'

    def add_arguments(self, parser):
        parser.add_argument('--app', type=str)
        parser.add_argument('--data', type=str)

    def handle(self, *args, **options):
        app_name = options['app']
        data_str = options['data']

        # print(app_name)
        # print(data_str)

        # Parse the JSON data
        restaurant_data = json.loads(data_str)

        

        for restaurant in restaurant_data:
            r = Restaurant.objects.create(id=uuid.uuid4().hex, name=restaurant['name'], cash_balance=restaurant['cash_balance'])
          
            for menu_item in restaurant['menu']:
                m = Menu.objects.create(restaurant_id=r.id, dish_name=menu_item['dish_name'], price=menu_item['price'])
            for opening_hours in restaurant['opening_hours']:
                oh = OpeningHours.objects.create(restaurant_id=r.id, day_of_week=opening_hours['day_of_week'],
                                                start_time=opening_hours['start_time'], end_time=opening_hours['end_time'])

