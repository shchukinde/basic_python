# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
# Решение через dict

try:
    while True:
        month = int(input('Введите номер месяца от 1 до 12(если хотите завершить програму введите 0(ноль)): '))
        if month == 0:
            quit()
        elif month > 12:
            print('Месяцев не может быть больше 12!')
        else:
            season = {1: "зимой", 2: "зимой", 3: "весной", 4: "весной", 5: "весной", 6: "летом", 7: "летом", 8: "летом", 9: "осенью", 10: "осенью", 11: "осенью",
              12: "зимой"}
            print("Этот месяц ", season.get(month))
except ValueError:
    print('Введено не число!')