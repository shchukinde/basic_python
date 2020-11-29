# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер ( для пальто) и рост ( для костюма) . Это могут быть обычные числа: V и
# H , соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property .

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calc_cloth(self):
        pass

class Coat(Clothes):
    def __init__(self,name, size):
        super().__init__(name) # проверка правильно ли я понял про super()
        self.size = size

    @property
    def calc_cloth(self):
        return self.size / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self,name, height):
        super().__init__(name) # проверка правильно ли я понял про super()
        self.height = height

    @property
    def calc_cloth(self):
        return self.height * 2 + 0.3

ct_1 = Coat("Пальтишко", 55)
st_1 = Suit("Костюмчик", 50)

print(f"Для {ct_1.name} размером {ct_1.size} потребуется {ct_1.calc_cloth} ткани")
print(f"Для {st_1.name} размером {st_1.height} потребуется {st_1.calc_cloth} ткани")

