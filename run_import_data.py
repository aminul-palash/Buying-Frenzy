import os
import json
import argparse
from django.core.management import execute_from_command_line
from data_process import DataProcess

# Set the Django settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_delivery.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'food_delivery.settings'

def run_import_data(user_data_file, restaurant_data_file):

    odp = DataProcess(restaurant_data=restaurant_data_file,users_data=user_data_file)
    user_data = odp.process_users_data()
    restaurant_data = odp.process_restaurant_data()
    
    # Call the management command with the data argument
    print("restaurant data importing ...")
    execute_from_command_line(['manage.py', 'import_restaurant_data', '--app', 'restaurant', '--data', json.dumps(restaurant_data)])
    print("users data importing ...")
    execute_from_command_line(['manage.py', 'import_user_data', '--app', 'user', '--data', json.dumps(user_data)])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--users_file", default="json_data/main_users.json", help="path to the users data file file")
    parser.add_argument("--restaurant_file", default="json_data/main_restaurant.json", help="path to the restaurant data file file")
    args = parser.parse_args()
   
    run_import_data(args.users_file, args.restaurant_file)
    print("data imported succesfully !")

if __name__ == "__main__":
    main()




