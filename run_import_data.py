import os
import json
from django.core.management import execute_from_command_line

# Set the Django settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_delivery.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'food_delivery.settings'

# Read the raw JSON data from a file or string
with open('json_data/users.json') as f:
    try:
        user_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        exit()

with open('json_data/restaurant_data.json') as f:
    try:
        restaurant_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        exit()


# Call the management command with the data argument
execute_from_command_line(['manage.py', 'import_restaurant_data', '--app', 'restaurant', '--data', json.dumps(restaurant_data)])
execute_from_command_line(['manage.py', 'import_user_data', '--app', 'user', '--data', json.dumps(user_data)])
