import requests
import allure
from API.base_function import BaseFunction
from data import API

class ActionCourier(BaseFunction):
    @allure.step('отправка формы POST на регистрацию нового курьера')
    def post_registration_courier(self, login = False, password = False, firstName = False):
        register_form = {}
        if login:
            register_form["login"] = login
        if password:
            register_form["password"] = password
        if firstName:
            register_form["firstName"] = firstName

        request = requests.post(
                    API.CREATE_COURIER,
                    json=register_form
                )
        return request

    @allure.step('отправка формы POST для входа курьером')
    def post_login_courier(self, login, password):
        login_form = {}
        if login:
            login_form["login"] = login
        if password:
            login_form["password"] = password
        

        request = requests.post(
                API.LOGIN_COURIER, 
                data=login_form
            )
        return request

    