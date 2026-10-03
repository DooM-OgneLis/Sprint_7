import allure

class BaseFunction:

    @allure.step('Проверить код запроса')
    def request_code_check(self, request, expected_code: int):
        if request.status_code == expected_code:
            return True
        else: return False

    @allure.step('Проверить тело запроса')
    def request_mesage_check(self, request, expected_code: int, data_request: dict):
        if request.json() == data_request[expected_code]:
            return True
        else: return False