import allure
import requests
from data import BASE_URL

@allure.step("Создание курьера")
def create_courier(payload):
    return requests.post(f'{BASE_URL}/api/v1/courier', json=payload)

@allure.step("Авторизация курьера")
def login_courier(login, password):
    payload = {"login": login, "password": password}
    return requests.post(f'{BASE_URL}/api/v1/courier/login', json=payload)

@allure.step("Удаление курьера")
def delete_courier(courier_id):
    return requests.delete(f'{BASE_URL}/api/v1/courier/{courier_id}')

@allure.step("Создание заказа")
def create_order(payload):
    return requests.post(f'{BASE_URL}/api/v1/orders', json=payload)

@allure.step("Получение списка заказов")
def get_orders():
    return requests.get(f'{BASE_URL}/api/v1/orders')

@allure.step("Отмена заказа по треку")
def cancel_order(track):
    return requests.put(f'{BASE_URL}/api/v1/orders/cancel', json={"track": track})