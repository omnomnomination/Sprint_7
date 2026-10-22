import allure
import pytest
from api import create_order, get_orders, cancel_order
from data import ORDER_COLORS

class TestOrderCreation:

    @allure.title("Создание заказа с разными вариантами цветов: {colors}")
    @pytest.mark.parametrize("colors", ORDER_COLORS)
    def test_order_creation_with_different_colors(self, colors):
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
        assert "track" in response.json()
        
        cancel_order(response.json()["track"])

    @allure.title("Проверка наличия поля track в ответе при создании заказа (цвета: {colors})")
    @pytest.mark.parametrize("colors", ORDER_COLORS)
    def test_order_creation_returns_track(self, created_order, colors):
        track = created_order(colors)
        assert isinstance(track, int)

    @allure.title("Проверка типа данных поля track в ответе (цвета: {colors})")
    @pytest.mark.parametrize("colors", ORDER_COLORS)
    def test_order_creation_body_contains_track(self, created_order, colors):
        track = created_order(colors)
        assert isinstance(track, int)

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = get_orders()
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)