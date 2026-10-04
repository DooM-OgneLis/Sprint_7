import allure
import pytest
import API.action_courier as AC
from data import API, Request, DinamicAllureCourier as DAC

class TestRegistrationCourier:

    @pytest.mark.parametrize(
            'status_code',[201, 409],
            ids=["new_user", "duplicate_user"]
            )
    def test_registration_courier_is(self, registration_data, status_code):
        action = AC.ActionCourier()
        request = action.post_registration_courier(registration_data[0], registration_data[1], registration_data[2])

        allure.dynamic.title(f"Проверка {DAC.DINAMIC_ALLURE_TITLE_IN_CODE[status_code]}")
        allure.dynamic.description(
            f"Отправить запрос POST на регистрацию нового курьера\n"
            f"Действие: отправка POST с данными: {registration_data} на {API.CREATE_COURIER}.\n"
            f"Ожидаемый результат: {DAC.DINAMIC_ALLURE_DESCRIPTION_IN_CODE[status_code]}"
        )

        assert action.request_code_check(request, status_code), (
            f"Код ответа не совпадает: ожидалось {status_code}, "
            f"получено {request.status_code}. URL: {request.url}"
        )
        assert action.request_mesage_check(request, status_code, Request.CREATE_COURIER), (
            f"Тело ответа не совпадает: ожидалось {Request.CREATE_COURIER[status_code]}, "
            f"получено {request.json()}. URL: {request.url}"
        )

    @allure.title('Проверка вывода ошибки при отправки формы без обязательного поля')
    @pytest.mark.parametrize(
        'modify_index',[0,1,2],
        ids=["no_login","no_password","no_firstName"]
        )
    def test_registration_courier_is_send_form_no_password_error_write_viev(self, registration_data, modify_index):
        action = AC.ActionCourier()
        reg_data = registration_data.copy()
        reg_data[modify_index] = False
        request = action.post_registration_courier(reg_data[0], reg_data[1], reg_data[2])

        status_code = 400

        allure.dynamic.description(
            f"Отправить запрос POST на регистрацию нового курьера\n"
            f"Действие: отправка POST с данными: {reg_data} на {API.CREATE_COURIER}.\n"
            f"Ожидаемый результат: возвращается ошибка с кодом 400 и сообщением {Request.CREATE_COURIER[status_code]}"
        )
        
        assert action.request_code_check(request, status_code), (
            f"Код ответа не совпадает: ожидалось {status_code}, "
            f"получено {request.status_code}. URL: {request.url}"
        )
        assert action.request_mesage_check(request, status_code, Request.CREATE_COURIER), (
            f"Тело ответа не совпадает: ожидалось {Request.CREATE_COURIER[status_code]}, "
            f"получено {request.json()}. URL: {request.url}"
        )

    
