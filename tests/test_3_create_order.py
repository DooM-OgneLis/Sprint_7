import allure
import pytest
from API.action_orders import ActionOrder as AO
from data import API


class TestCreateOrder:

    @pytest.mark.parametrize(
        'color',[False, ['BLACK'], ['GREY'], ['BLACK', 'GREY']],
        ids=["no_color", "black", "grey", "black_and_gray"]
        )
    def test_create_order_complite(self, data_form_order, color):

        create_order = AO()
        modify = create_order.modify_add_data_list(data_form_order, "color", color)

        request = create_order.add_order_list(data_form_order)
        allure.dynamic.title(f'Создания заказа на самокат с параметром цвета {color}')
        allure.dynamic.description(
            f"Отправить запрос POST на регистрацию нового курьера\n"
            f"Действие: отправка POST с данными: {modify} на {API.ORDER_COURIER}.\n"
            f"Ожидаемый результат: заказ оформлен, получен код 201 с сообщением track: номер_заказа"
        )

        status_code = 201

        assert create_order.request_code_check(request, status_code), (
                    f"Код ответа не совпадает: ожидалось {status_code}, "
                    f"получено {request.status_code}. URL: {request.url}"
                )
        assert 'track' in request.json(), ('В теле ответа отсутствует поле track')
