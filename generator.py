import random
from datetime import timedelta, date
from faker import Faker

fake = Faker()
fake.address
def login_generator():
    """Генерирует случайное имя пользователя"""
    generated_login = fake.user_name() + str(random.randint(1000, 9999))
    return generated_login

def password_generator():
    """Генерирует случайный пароль (только буквы и цифры)"""
    generated_password = fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True)
    return generated_password

def name_generator():
    """Генерирует случайное имя"""
    generated_name = fake.first_name()
    return generated_name

def last_name_generator():
    """Генерирует случайное имя"""
    generated_name = fake.last_name()
    return generated_name

def adress_generator():
    generated_adress = fake.address()
    return generated_adress

def random_phone():
    return f"+79{random.randint(10000000, 99999999)}"

def random_index_metroStation():
    return random.randint(1, 9)

def random_date_for_delivery():
    today = date.today()
    offset = random.randint(1, 14)
    return (today + timedelta(days=offset)).strftime("%Y-%m-%d")