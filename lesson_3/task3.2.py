# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.

def user_info_func (name, surname, year, city, email, tel_number):
    print(f'Зарегистрирован {name} {surname} {year} г.р. проживающий в городе {city}. ' \
           f'С ним можно связаться по телефону {tel_number} или электронной почте {email}')

user_name = input('Введите имя:')
user_surname = input('Введите фамилию:')
user_year = input('Введите год рождения:')
user_city = input('Введите город проживания:')
user_email = input('Введите адрес электронной почты:')
user_tel = input('Введите телефонный номер:')

user_info_func(name=user_name,surname=user_surname, year=user_year,city=user_city,email=user_email,tel_number=user_tel)