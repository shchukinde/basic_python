# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

numbers = input("Введите числа через пробел, они будут записаны в файл task5.5.txt:")

with open('task5.5.txt', "w", encoding='utf-8') as f_obj:
    f_obj.write(numbers)

with open('task5.5.txt', "r", encoding='utf-8') as f_obj:
    line = f_obj.readline()

print("Программа завершена. Сумма чисел в файле task5.5.txt: ", sum(map(int, line.split())))