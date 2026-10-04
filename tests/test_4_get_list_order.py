import allure
import API.action_orders as AO
from data import API

class TestGetOrder:

    @allure.title('запрос списка заказов')
    @allure.description(
        f'Запрос GET на {API.ORDER_COURIER}'
        'ожидаемый результат: получен код 200 и список заказов'
        )
    def test_get_list_orders_in_body_request(self):
        order = AO.ActionOrder()
        status_code = 200
        request = order.get_order_list(None, None, '3')

        assert order.request_code_check(request, status_code), (
            f"Код ответа не совпадает: ожидалось {status_code}, "
            f"получено {request.status_code}. URL: {request.url}"
        )
        assert 'orders' in request.json(), ('В теле ответа отсутствует поле orders')
        assert 'pageInfo' in request.json(), ('В теле ответа отсутствует поле pageInfo')
        assert 'availableStations' in request.json(), ('В теле ответа отсутствует поле availableStations')