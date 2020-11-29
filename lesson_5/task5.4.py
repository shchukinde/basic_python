# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

lines_list = []
new_list = []

numbers_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('task5.4.txt', "r", encoding='utf-8') as f_obj:
    lines_list = f_obj.readlines()

for el in lines_list:
    temp_list = el.split()
    new_list.append(f'{numbers_dict[temp_list[0]]} - {temp_list[2]}\n')

with open('task5.4_new.txt', "w", encoding='utf-8') as f_obj:
     f_obj.writelines(new_list)

print("Программа завершена. Результат в файле task5.4_new.txt")