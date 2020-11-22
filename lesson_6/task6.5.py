# Реализовать класс Stationery ( канцелярская принадлежность). Определить в нем атрибут t itle
# (название) и метод draw ( отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen ( ручка), Pencil ( карандаш), Handle ( маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки."

class Pen(Stationery):
    def draw(self):
        return "Запуск отрисовки ручкой"

class Pencil(Stationery):
    def draw(self):
        return "Запуск отрисовки карандашом"

class Handle(Stationery):
    def draw(self):
        return "Запуск отрисовки маркером"

stationery1 = Stationery("Канцелярия")
pen1 = Pen("Ручка")
pencil1 = Pencil("Карандаш")
handle1 = Handle("Маркер")

print(stationery1.draw())
print(pen1.draw())
print(pencil1.draw())
print(handle1.draw())


