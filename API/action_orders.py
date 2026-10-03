import requests
import allure
from API.base_function import BaseFunction
from data import API

class ActionOrder(BaseFunction):

    @allure.step('создать новый заказ')
    def add_order_list(self, data_list):
        request = requests.post(
                API.ORDER_COURIER,
                json=data_list
            )
        return request
    
    @allure.step('получить список заказов')
    def get_order_list(self, courierId = False, nearestStation = False, limit = False, page = False):
        get_filter = []
        str_filter = ''
        if courierId:
            get_filter.append('courierId='+courierId)
        if nearestStation:
            get_filter.append('nearestStation='+nearestStation)
        if limit:
            get_filter.append('limit='+limit)
        if page:
            get_filter.append('page='+page)

        if len(get_filter) > 0:
            for i, obj in enumerate(get_filter):
                if i == 0:
                    str_filter += f'?{obj}'
                else:
                    str_filter += f'&{obj}'

        request = requests.get(
                    API.ORDER_COURIER+str_filter,
                    json=get_filter
                )
        return request
