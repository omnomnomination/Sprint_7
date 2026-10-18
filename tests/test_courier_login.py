import requests
from data import BASE_URL
from helpers.utils import generate_courier_payload, login_courier, delete_courier

# ==============================
# Блок "авторизация курьера"
# ==============================

def test_courier_can_login():
    payload = generate_courier_payload()
    requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    response = login_courier(payload["login"], payload["password"])
    assert response.status_code == 200
    delete_courier(response.json()["id"])

def test_login_requires_all_fields():
    payload = generate_courier_payload()
    requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    response = requests.post(f'{BASE_URL}/api/v1/courier/login', json={"login": payload["login"]})
    assert response.status_code == 400
    login_response = login_courier(payload["login"], payload["password"])
    delete_courier(login_response.json()["id"])

def test_login_wrong_credentials_returns_error():
    payload = generate_courier_payload()
    requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    response = login_courier(payload["login"], "wrong_password")
    assert response.status_code == 404
    login_response = login_courier(payload["login"], payload["password"])
    delete_courier(login_response.json()["id"])

def test_login_missing_field_returns_error():
    payload = generate_courier_payload()
    requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    response = requests.post(f'{BASE_URL}/api/v1/courier/login', json={"password": payload["password"]})
    assert response.status_code == 400
    login_response = login_courier(payload["login"], payload["password"])
    delete_courier(login_response.json()["id"])

def test_login_non_existent_user_returns_error():
    payload = generate_courier_payload()
    response = login_courier(payload["login"], payload["password"])
    assert response.status_code == 404

def test_login_returns_id():
    payload = generate_courier_payload()
    requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    response = login_courier(payload["login"], payload["password"])
    assert "id" in response.json()
    delete_courier(response.json()["id"])