import random
import string
import requests
from data import BASE_URL

# Создание курьера
def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_courier_payload():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }

# Авторизация курьера
def login_courier(login, password):
    return requests.post(f'{BASE_URL}/api/v1/courier/login', json={
        "login": login,
        "password": password
    })

# Удаление курьера
def delete_courier(courier_id):
    requests.delete(f'{BASE_URL}/api/v1/courier/{courier_id}')

# Создание заказа
def create_order(payload):
    return requests.post(f'{BASE_URL}/api/v1/orders', json=payload)