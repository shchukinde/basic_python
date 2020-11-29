# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

lines_list = []

with open('task5.3.txt', "r", encoding='utf-8') as f_obj:
    lines_list = f_obj.readlines()

poor_man_list = [i.split()[0] for i in lines_list if float(i.split()[1]) < 20000]
all_wage_list = [float(i.split()[1]) for i in lines_list]

print("Сотрудники с з\п менее 20000:\n", poor_man_list)
print("Cредний доход сотрудников составляет:", round(sum(all_wage_list) / len(all_wage_list), 2))