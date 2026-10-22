import allure
from api import create_courier, login_courier, delete_courier
from helpers.utils import generate_courier_payload

class TestCourierCreation:

    @allure.title("Успешное создание курьера")
    def test_courier_can_be_created(self):
        payload = generate_courier_payload()
        create_response = create_courier(payload)
        assert create_response.status_code == 201
        assert create_response.json() == {"ok": True}
        
        login_response = login_courier(payload["login"], payload["password"])
        assert login_response.status_code == 200
        delete_courier(login_response.json()["id"])

    @allure.title("Проверка невозможности создать двух одинаковых курьеров")
    def test_cannot_create_two_identical_couriers(self, new_courier):
        duplicate_response = create_courier(new_courier)
        assert duplicate_response.status_code == 409
        assert "message" in duplicate_response.json()

    @allure.title("Создание курьера без обязательного поля (логин)")
    def test_create_courier_requires_all_fields(self):
        payload = generate_courier_payload()
        del payload["login"]
        response = create_courier(payload)
        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Проверка возвращаемого кода ответа при создании курьера")
    def test_create_courier_returns_correct_status_code(self):
        payload = generate_courier_payload()
        response = create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        
        login_response = login_courier(payload["login"], payload["password"])
        delete_courier(login_response.json()["id"])

    @allure.title("Проверка возвращаемого тела ответа ok True при создании курьера")
    def test_create_courier_returns_ok_true(self):
        payload = generate_courier_payload()
        response = create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        
        login_response = login_courier(payload["login"], payload["password"])
        delete_courier(login_response.json()["id"])

    @allure.title("Ошибка при создании курьера без пароля")
    def test_create_courier_missing_field_returns_error(self):
        payload = generate_courier_payload()
        del payload["password"]
        response = create_courier(payload)
        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Ошибка при создании курьера с уже существующим логином")
    def test_create_courier_existing_login_returns_error(self, new_courier):
        new_payload = generate_courier_payload()
        new_payload["login"] = new_courier["login"]
        response = create_courier(new_payload)
        assert response.status_code == 409
        assert "message" in response.json()