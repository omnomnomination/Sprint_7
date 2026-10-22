import pytest
from api import create_courier, login_courier, delete_courier, create_order, cancel_order
from helpers.utils import generate_courier_payload

@pytest.fixture
def new_courier():
    payload = generate_courier_payload()
    create_courier(payload)
    yield payload
    
    login_response = login_courier(payload["login"], payload["password"])
    if login_response.status_code == 200:
        delete_courier(login_response.json()["id"])

@pytest.fixture
def created_order(request):
    def _create_order(colors):
        order_payload = {
            "firstName": "Test",
            "lastName": "Test",
            "address": "Test",
            "metroStation": 1,
            "phone": "79999999999",
            "rentTime": 1,
            "deliveryDate": "2024-12-31",
            "comment": "Test",
            "color": colors
        }
        response = create_order(order_payload)
        track = response.json()["track"]
        
        request.addfinalizer(lambda: cancel_order(track))
        
        return track
        
    return _create_order