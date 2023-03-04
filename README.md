
## Installation

### Python Version

- Python == 3.8.10

### Virtual Environment


#### Linux

- `python -m venv venv`
- `source venv/bin/activate`

If you want to setup from this repository then run bellow command:
```bash
git colne https://github.com/aminul-palash/drf_assignment_pillar.git
cd drf_assignment_pillar

```
Finaly run the following command to ensure that everything is being installed correctly.
```bash
pip install -r requirements.txt
```
## Run Server

To run server
Activate the virtual environment and run the below command from project directory.

```
python manage.py runserver

```
# API Instruction

Instruction for api is given [here]().

## 1. API root url

```
http://127.0.0.1:8000/api

```
This will return list of users with purchase history data..

To navigate specific page of data parse query parameter 'p'. For example

```
http://127.0.0.1:8000/api/?p=page_number

```

## 2. Search restaurant by date time

This RESTful API endpoint provides a list of restaurants that are available at a specific date and time. It accepts two query parameters:

* [date:](#) A string in the format YYYY-MM-DD that specifies the date for which the available restaurants are being searched.
* [time:](#) A string in the format HH:MM:SS that specifies the time for which the available restaurants are being searched.

### Request Example

```
http://localhost:8000/api/restaurants/bydatetime/?date=2023-03-06&time=18:00:00

```

### Response Example

```
HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "id": "89a8d37b-4eda-4068-ab85-d9dd0aa60177",
        "name": "'Ulu Ocean Grill and Sushi Lounge",
        "cash_balance": "4483.84",
        "menus": [
            {
                "id": 1,
                "dish_name": "Postum cereal coffee",
                "price": "13.88",
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177"
            },
            {
                "id": 1,
                "dish_name": "Postum cereal coffee",
                "price": "13.88",
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177"
            }
        ]
    },

    {
        "id": "89a8d37b-4eda-4068-ab85-d9dd0aa60177",
        "name": "'Ulu Ocean Grill and Sushi Lounge",
        "cash_balance": "4483.84",
        "menus": [
            {
                "id": 1,
                "dish_name": "Postum cereal coffee",
                "price": "13.88",
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177"
            },
            {
                "id": 1,
                "dish_name": "Postum cereal coffee",
                "price": "13.88",
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177"
            }
        ]
    }

]

```
The response is a JSON array of restaurant objects that match the specified date and time criteria.

## 3. Top Restaurant

The URL http://localhost:8000/api/top-restaurants/ appears to be a RESTful API endpoint that retrieves a list of top-rated restaurants based on certain filters. It accepts five query parameters:

* [more_than:](#) An integer that specifies the minimum number of menu for the restaurants. In this case, the value is 10.
* [less_than:](#) An integer that specifies the maximum number of menu for the restaurants. In this case, the value is 50.
* [min_price:](#) A float that specifies the minimum price value of menu for the restaurants to be included in the results. In this case, the value is 10.
* [max_price:](#) A float that specifies the maximum price value of menu for the restaurants to be included in the results. In this case, the value is 30.
* [y:](#) List top y restaurants .

### Request Example

```
http://localhost:8000/api/top-restaurants/?more_than=10&less_than=50&min_price=10&max_price=30&y=5

```

### Response Example

```
HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "id": "89a8d37b-4eda-4068-ab85-d9dd0aa60177",
        "name": "'Ulu Ocean Grill and Sushi Lounge",
        "cash_balance": "4483.84",
        "menus": [
            {
                "id": 1,
                "dish_name": "Postum cereal coffee",
                "price": "13.88",
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177"
            }
            ....
        ],
        "opening_hours": [
            {
                "id": 1,
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177",
                "day_of_week": 0,
                "start_time": "14:30:00",
                "end_time": "20:00:00"
            }
            ....
        ]
    },
    {
        "id": "89a8d37b-4eda-4068-ab85-d9dd0aa60177",
        "name": "'Ulu Ocean Grill and Sushi Lounge",
        "cash_balance": "4483.84",
        "menus": [
            {
                "id": 1,
                "dish_name": "Postum cereal coffee",
                "price": "13.88",
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177"
            }
            ....
        ],
        "opening_hours": [
            {
                "id": 1,
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177",
                "day_of_week": 0,
                "start_time": "14:30:00",
                "end_time": "20:00:00"
            }
            ....
        ]
    }
]

```
The response is a JSON array of restaurant objects that match the specified filters.

## 4. Search Restaurant by restaurant name or dish name

The URL http://localhost:8000/api/restaurants/search/?q=text is a RESTful API endpoint that allows searching for restaurants based on a text query string.

The endpoint accepts a single query parameter q which represents the text query to search for. This query parameter can include the name of the restaurant or the name of a dish served at the restaurant. For example, if the query parameter is set to italian pasta, the API will return a list of all the restaurants that serve Italian cuisine and have pasta dishes on their menu.

### Request Example

```
http://localhost:8000/api/restaurants/search/?q=Sushi

```

## Response Example

```
HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "id": "89a8d37b-4eda-4068-ab85-d9dd0aa60177",
        "name": "'Ulu Ocean Grill and Sushi Lounge",
        "cash_balance": "4483.84",
        "menus": [
            {
                "id": 1,
                "dish_name": "Postum cereal coffee",
                "price": "13.88",
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177"
            }
            ....
        ],
        "opening_hours": [
            {
                "id": 1,
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177",
                "day_of_week": 0,
                "start_time": "14:30:00",
                "end_time": "20:00:00"
            }
            ....
        ]
    },
    {
        "id": "89a8d37b-4eda-4068-ab85-d9dd0aa60177",
        "name": "'Ulu Ocean Grill and Sushi Lounge",
        "cash_balance": "4483.84",
        "menus": [
            {
                "id": 1,
                "dish_name": "Postum cereal coffee",
                "price": "13.88",
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177"
            }
            ....
        ],
        "opening_hours": [
            {
                "id": 1,
                "restaurant": "89a8d37b-4eda-4068-ab85-d9dd0aa60177",
                "day_of_week": 0,
                "start_time": "14:30:00",
                "end_time": "20:00:00"
            }
            ....
        ]
    }
]

```
The response is a JSON array of restaurant objects that match the specified text query. \

## Food Ordering Restaurant API
This is an API for ordering food from various restaurants.
### Endpoint
POST /api/purchase/
This endpoint allows users to purchase a menu item from a restaurant.

### Request
The request must include a JSON payload with the following fields:

* [username:](#) The username of the user making the purchase.
* [restaurant_name:](#) The name of the restaurant where the menu item is being purchased from.
* [menu_item_name:](#) The name of the menu item being purchased.

### Example request

```
curl --location --request POST 'http://localhost:8000/api/purchase/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "john_doe",
    "restaurant_name": "McDonald's",
    "menu_item_name": "Big Mac"
}'

```

### Response
If the purchase is successful, the server will respond with a JSON payload containing the following fields:

[message:](#) A success message.
[restaurant_cash_balance:](#) The cash balance of the restaurant after the purchase.
[user_cash_balance:](#) The cash balance of the user after the purchase.
[purchase:](#) Information about the purchase, including the ID of the purchase, the username of the user making the purchase, the name of the restaurant where the menu item is being purchased from, the name of the menu item being purchased, and the date and time of the purchase.

### Example response:

```
{
    "message": "Purchase successful",
    "restaurant_cash_balance": 569.98,
    "user_cash_balance": 688.26,
    "purchase": {
        "id": 9309,
        "user": 1,
        "restaurant": "51fa108c-6038-44d0-a5fa-f58ac7b61c2f",
        "menu": 194,
        "transaction_amount": "12.44",
        "transaction_date": "2023-03-04T15:09:00.765800Z"
    }
}

```
If there is an error with the request, the server will respond with an appropriate error message and status code.










