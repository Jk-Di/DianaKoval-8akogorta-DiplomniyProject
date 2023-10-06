import requests
import response

import configuration
import data

def post_order():
    response = requests.post(configuration.BASE_URL + configuration.ORDERS_API_PATH,
    json=data.order_body)
    print("Response from post_order:", response.text)
    return response

response = post_order()