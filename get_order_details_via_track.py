# Диана Коваль, 8а когорта — Финальный проект. Инженер по тестированию плюс

import requests
import configuration
import sender_stand_request

def get_track():
    track = sender_stand_request.response.json().get("track")
    return track
print(get_track())

def get_order_by_track():
    track = str(get_track())
    response = requests.get(configuration.BASE_URL + configuration.ORDERS_API_PATH + track)
    return response

def test_status_code():
    order_response = get_order_by_track()
    print("Response content:", order_response.text)
    assert order_response.status_code == 200

test_status_code()