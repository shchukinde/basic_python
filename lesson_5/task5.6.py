# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

lines_list = []
my_dict = {}

with open('task5.6.txt', "r", encoding='utf-8') as f_obj:
    lines_list = f_obj.readlines()

for el in lines_list:
    el = el.replace(':','')
    el = el.replace('—','')
    el = el.replace('(л)','')
    el = el.replace('(пр)','')
    el = el.replace('(лаб)','')
    temp_list = el.split()
    my_dict[temp_list[0]] = sum(map(int, temp_list[1:]))

print(my_dict)