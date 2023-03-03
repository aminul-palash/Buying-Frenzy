from django.core.management.base import BaseCommand
import json,uuid
import datetime
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
            
            r = Restaurant.objects.create(id=uuid.uuid4().hex, name=restaurant['restaurantName'], cash_balance=restaurant['cashBalance'])
          
            for menu_item in restaurant['menu']:
                m = Menu.objects.create(restaurant_id=r.id, dish_name=menu_item['dishName'], price=menu_item['price'])
           
            for opening_hours in restaurant['openingHours']:
                
                opening_hours['start_time'] = datetime.datetime.strptime(opening_hours['start_time'], "%H:%M").time()
                opening_hours['end_time'] = datetime.datetime.strptime(opening_hours['end_time'], "%H:%M").time()
                oh = OpeningHours.objects.create(restaurant_id=r.id, day_of_week=opening_hours['day_of_week'],
                                                start_time=opening_hours['start_time'], end_time=opening_hours['end_time'])

