#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.
n = int(input('Введите число: '))
max_number = 0

while n > 1:
    number = n % 10
    if number > max_number:
        max_number = number
    n = n // 10

print('Самая большая цифра', max_number)