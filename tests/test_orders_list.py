import allure
from api import get_orders

class TestOrdersList:
    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = get_orders()
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)