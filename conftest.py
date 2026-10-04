import pytest
import generator

@pytest.fixture(scope="session")
def registration_data():
    login = generator.login_generator()
    password = generator.password_generator()
    firstName = generator.name_generator()
    return [
        login,
        password,
        firstName
    ]

@pytest.fixture(scope="function") #для проверки формы подходит, каждый раз новые данные
def data_form_order():
    return {
        "firstName": generator.name_generator(),
        "lastName": generator.last_name_generator(),
        "address": generator.adress_generator(),
        "metroStation": generator.random_index_metroStation(),        
        "deliveryDate": generator.random_date_for_delivery(),
        "phone": generator.random_phone(),
        "rentTime": 3,
        "comment": "hello",
        "color": []
    }