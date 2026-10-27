import allure
import pytest
from api import create_order, cancel_order
from data import ORDER_COLORS

class TestOrderCreation:

    @allure.title("Создание заказа с разными вариантами цветов: {colors}")
    @pytest.mark.parametrize("colors", ORDER_COLORS)
    def test_order_creation_with_different_colors(self, colors, request):
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
        

        request.addfinalizer(lambda: cancel_order(response.json()["track"]))
        
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Проверка наличия поля track в ответе при создании заказа (цвета: {colors})")
    @pytest.mark.parametrize("colors", ORDER_COLORS)
    def test_order_creation_returns_track(self, created_order, colors):
        response, track = created_order(colors)
        assert response.status_code == 201
        assert track is not None

    @allure.title("Проверка типа данных поля track в ответе (цвета: {colors})")
    @pytest.mark.parametrize("colors", ORDER_COLORS)
    def test_order_creation_body_contains_track(self, created_order, colors):
        response, track = created_order(colors)
        assert response.status_code == 201
        assert isinstance(track, int)

