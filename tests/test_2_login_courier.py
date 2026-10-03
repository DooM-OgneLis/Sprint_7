import allure
import API.action_courier as AC
from data import API, Request

class TestLoginCourier:

    @allure.title('Выполнение входа в учетную запись')
    def test_login_courier_access_complite_return_id_key(self, registration_data):
        action = AC.ActionCourier()
        request = action.post_login_courier(registration_data[0], registration_data[1])
        status_code = 200
        
        allure.dynamic.description(
            f"Отправить запрос POST на вход в аккаунт курьера\n"
            f"Действие: отправка POST с данными: {registration_data[0], registration_data[1]} на {API.LOGIN_COURIER}.\n"
            f"Ожидаемый результат: получен ответ id: id_user"
        )

        assert action.request_code_check(request, status_code), (
            f"Код ответа не совпадает: ожидалось {status_code}, "
            f"получено {request.status_code}. URL: {request.url}"
        )
        assert  'id' in request.json(), ('В теле ответа отсутствует поле id')

    
    @allure.title('Выполнение входа в несуществующую учетную запись')
    def test_login_undentiffed_courier_access_denite_return_error_msg(self, registration_data):
        action = AC.ActionCourier()
        request = action.post_login_courier('vasya_pupkin9999999', registration_data[1])
        status_code = 404
        
        allure.dynamic.description(
            f"Отправить запрос POST на вход в аккаунт курьера\n"
            f"Действие: отправка POST с данными: {registration_data[0], registration_data[1]} на {API.LOGIN_COURIER}.\n"
            f"Ожидаемый результат: возвращается ошибка с кодом 404 и сообщением {Request.LOGIN_COURIER[status_code]}"
        )

        assert action.request_code_check(request, status_code), (
            f"Код ответа не совпадает: ожидалось {status_code}, "
            f"получено {request.status_code}. URL: {request.url}"
        )
        assert action.request_mesage_check(request, status_code, Request.LOGIN_COURIER), (
            f"Тело ответа не совпадает: ожидалось {Request.LOGIN_COURIER[status_code]}, "
            f"получено {request.json()}. URL: {request.url}"
        )

    @allure.title('Выполнение входа с неправильным паролем')
    def test_login_courier_incorrect_password_access_denite_return_error_msg(self, registration_data):
        action = AC.ActionCourier()
        request = action.post_login_courier(registration_data[0], 'qwertyuiop')
        status_code = 404
        
        allure.dynamic.description(
            f"Отправить запрос POST на вход в аккаунт курьера\n"
            f"Действие: отправка POST с данными: {registration_data[0]}, 'qwertyuiop' на {API.LOGIN_COURIER}.\n"
            f"Ожидаемый результат: возвращается ошибка с кодом 404 и сообщением {Request.LOGIN_COURIER[status_code]}"
        )

        assert action.request_code_check(request, status_code), (
            f"Код ответа не совпадает: ожидалось {status_code}, "
            f"получено {request.status_code}. URL: {request.url}"
        )
        assert action.request_mesage_check(request, status_code, Request.LOGIN_COURIER), (
            f"Тело ответа не совпадает: ожидалось {Request.LOGIN_COURIER[status_code]}, "
            f"получено {request.json()}. URL: {request.url}"
        )

    @allure.title('Выполнение входа в учетную запись без поля пароль')
    def test_login_courier_no_password_access_denite_return_error_msg(self, registration_data):
        action = AC.ActionCourier()
        request = action.post_login_courier(registration_data[0], False)
        status_code = 400
        
        allure.dynamic.description(
            f"Отправить запрос POST на вход в аккаунт курьера\n"
            f"Действие: отправка POST с данными: {registration_data[0]} на {API.LOGIN_COURIER}.\n"
            f"Ожидаемый результат: возвращается ошибка с кодом 400 и сообщением {Request.LOGIN_COURIER[status_code]}"
        )
        #в postman ситуация та-же, после timeout выходит ошибка 504, эмулировать через мок нельзя, так как результат будет недостоверным
        assert action.request_code_check(request, status_code), (
            f"Код ответа не совпадает: ожидалось {status_code}, "
            f"получено {request.status_code}. URL: {request.url}"
        )
        assert action.request_mesage_check(request, status_code, Request.LOGIN_COURIER), (
            f"Тело ответа не совпадает: ожидалось {Request.LOGIN_COURIER[status_code]}, "
            f"получено {request.json()}. URL: {request.url}"
        )