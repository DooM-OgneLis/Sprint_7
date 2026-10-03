

class URL:
    SCOOTER = 'https://qa-scooter.praktikum-services.ru'

class API:
    CREATE_COURIER = URL.SCOOTER+'/api/v1/courier'
    LOGIN_COURIER = CREATE_COURIER+'/login'
    ORDER_COURIER = URL.SCOOTER+'/api/v1/orders'
    
class Request:
    #запросы на действия с курьером
    CREATE_COURIER = {
        201: {'ok': True},
        400: {'message': 'Недостаточно данных для создания учетной записи'},
        409: {'message': 'Этот логин уже используется'}
    }

    LOGIN_COURIER = {
        400: {"message": "Недостаточно данных для входа"},
        404: {"message": "Учетная запись не найдена"}
    }

class DinamicAllureCourier:
    DINAMIC_ALLURE_TITLE_IN_CODE = {
        200: 'успешного входа в аккаунт',
        201: 'успешного создания учетной записи',
        404: 'вывода ошибки при входе в аккаунт с несуществующим логином',
        409: 'вывода ошибки при использовании уже существующего логина'
    }

    DINAMIC_ALLURE_DESCRIPTION_IN_CODE = {
        200: 'запрос вернул ответ код: 200 с сообщением id УЗ',
        201: 'учетная запись создана, положительный ответ с кодом 201 получен',
        404: f'запрос вернул ошибку с кодом 404 и сообщением {Request.LOGIN_COURIER[404]}',
        409: f'возвращается ошибка с кодом 409 и сообщением {Request.CREATE_COURIER[409]}'
    }

class DinamicAllureOrder:
    DINAMIC_ALLURE_TITLE_IN_CODE = {
        201: 'заказ оформлен, в сообщении вернулся трекер с номером заказа',
        400: 'в форме неправильно заполнено обязательное поле или оно отсутствует'
    }

    DINAMIC_ALLURE_DESCRIPTION_IN_CODE = {
        201: 'получен код 201 с сообщением "track: номер_заказа',
        400: ['Отправка запроса без обязательного поля {}','возвращается ошибка с кодом 400, message: "Bad Request"']
            
    }