# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    my_list = [x, y, z]
    my_list.sort()
    return my_list[1]+my_list[2]

number_x = int(input('Введите первое число:'))
number_y = int(input('Введите второе число:'))
number_z = int(input('Введите третье число:'))

print("Сумма двух наибольших чисел равна: ", my_func(number_x, number_y, number_z))
