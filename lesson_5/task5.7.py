# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка,
# издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
# Подсказка: использовать менеджер контекста.

import json

lines_list = []
firm_dict = {}

with open('task5.7.txt', "r", encoding='utf-8') as f_obj:
    lines_list = f_obj.readlines()

profit_firm_list = [i[:-1] for i in lines_list if int(i.split()[2]) - int(i.split()[3]) > 0 ]
average_profit = sum([int(i.split()[2]) - int(i.split()[3]) for i in profit_firm_list]) / len(profit_firm_list)

firm_dict = {i.split()[0] : (int(i.split()[2]) - int(i.split()[3])) for i in lines_list}

final_list =[firm_dict, {"average_profit" : average_profit}]

with open('task5.7.json', 'w', encoding='utf-8') as f_json:
    json.dump(final_list, f_json, ensure_ascii=False, indent=4)

print("Список ниже сохранили в файл task5.7.json\n", final_list)