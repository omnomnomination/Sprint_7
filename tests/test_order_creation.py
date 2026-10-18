import pytest
import requests
from data import BASE_URL, ORDER_COLORS
from helpers.utils import create_order

@pytest.mark.parametrize("colors", ORDER_COLORS)
def test_order_creation_with_different_colors(colors):
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
    assert response.status_code == 201

@pytest.mark.parametrize("colors", ORDER_COLORS)
def test_order_creation_returns_track(colors):
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
    assert "track" in response.json()

@pytest.mark.parametrize("colors", ORDER_COLORS)
def test_order_creation_body_contains_track(colors):
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
    assert isinstance(response.json().get("track"), int)

def test_get_orders_list():
    response = requests.get(f'{BASE_URL}/api/v1/orders')
    assert response.status_code == 200