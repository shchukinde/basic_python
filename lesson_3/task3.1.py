# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

def division_func(a, b):
    """
    :param a: int number
    :param b: int number
    :return: a / b
    """
    if b == 0:
        return 'На ноль делить нельзя!'
    else:
        return round(a / b,3)

number1 = int(input('Введите делимое:'))
number2 = int(input('Введите делитель:'))
print("Результат: ", division_func(number1, number2))