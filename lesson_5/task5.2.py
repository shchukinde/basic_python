# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.
lines_list = []
sum_words = 0

with open('task5.2.txt', "r", encoding='utf-8') as f_obj:
    lines_list = f_obj.readlines()

for el in lines_list:
   sum_words += len(el.split())
print("Количество строк: ", len(lines_list))
print("Количество слов: ", sum_words)