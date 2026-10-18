import requests
from data import BASE_URL
from helpers.utils import generate_courier_payload, login_courier, delete_courier

# ===================================
# Блок "создание курьера"
# ===================================

def test_courier_can_be_created():
    payload = generate_courier_payload()
    requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    response = login_courier(payload["login"], payload["password"])
    assert response.status_code == 200
    delete_courier(response.json()["id"])

def test_cannot_create_two_identical_couriers():
    payload = generate_courier_payload()
    requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    duplicate_response = requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    assert duplicate_response.status_code == 409
    login_response = login_courier(payload["login"], payload["password"])
    delete_courier(login_response.json()["id"])

def test_create_courier_requires_all_fields():
    payload = generate_courier_payload()
    del payload["login"]
    response = requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    assert response.status_code == 400

def test_create_courier_returns_correct_status_code():
    payload = generate_courier_payload()
    response = requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    assert response.status_code == 201
    login_response = login_courier(payload["login"], payload["password"])
    delete_courier(login_response.json()["id"])

def test_create_courier_returns_ok_true():
    payload = generate_courier_payload()
    response = requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    assert response.json() == {"ok": True}
    login_response = login_courier(payload["login"], payload["password"])
    delete_courier(login_response.json()["id"])

def test_create_courier_missing_field_returns_error():
    payload = generate_courier_payload()
    del payload["password"]
    response = requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    assert response.status_code == 400

def test_create_courier_existing_login_returns_error():
    payload = generate_courier_payload()
    requests.post(f'{BASE_URL}/api/v1/courier', json=payload)
    new_payload = generate_courier_payload()
    new_payload["login"] = payload["login"]
    response = requests.post(f'{BASE_URL}/api/v1/courier', json=new_payload)
    assert response.status_code == 409
    login_response = login_courier(payload["login"], payload["password"])
    delete_courier(login_response.json()["id"])

