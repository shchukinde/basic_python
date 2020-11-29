# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

text_line = ''
text_list = []

while True:
    text_line = input("Введите строку текста.(Если ничего не будет введно и нажат Enter, то программа будет завершена):")
    text_line +='\n'
    if text_line == '\n':
        break
    text_list.append(text_line)
    print(text_line)

with open('task5.1.txt', "w", encoding='utf-8') as f_obj:
    txt = f_obj.writelines(text_list)

print("Программа завершена")
