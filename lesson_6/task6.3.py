# Реализовать базовый класс Worker ( работник), в котором определить атрибуты: name,
# surname, position ( должность), income ( доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position ( должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника ( get_full_name) и
# дохода с учетом премии ( get_total_income) . Проверить работу примера на реальных данных
# (создать экземпляры класса Position , передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker():
    def __init__(self, name, surname, income):
        self.name = name
        self.surname = surname
        self._income = income

class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

p_name = input("Введите имя сотрудника: ")
p_surname = input("Введите фамилию сотрудника: ")
p_wage = float(input("Введите размер оклада: "))
p_bonus = float(input("Введите размер премии: "))
p_income = {"wage": p_wage, "bonus": p_bonus}

pos1 = Position(p_name, p_surname, p_income)

print("Полное имя сотрудника", pos1.get_full_name())
print("Доход сотрудника с учётом премии", pos1.get_total_income())