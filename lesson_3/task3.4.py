# Программа принимает действительное положительное число x и целое отрицательное число
# y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
# в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
def my_func(x, y):
    return x**y

def my_func_v_2(x, y):
    z = 1
    while y < 0:
        y += 1
        z *= x
    return 1 / z

number_x = float(input('Введите действительное положительное число:'))
number_y = int(input('Введите отрицательное целое число:'))

print(f'Результат работы my_func {number_x}^({number_y}) = {my_func(number_x, number_y)}')
print(f'Результат работы my_func_v2 {number_x}^({number_y}) = {my_func_v_2(number_x, number_y)}')