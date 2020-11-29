# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police ( булево). А также методы: go, stop, t urn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# ( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self, name, color, speed = 0, is_police = False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return "поехала"

    def stop(self):
        return "остановилась"

    def turn(self, direction):
        return "повернула "+direction

    def show_speed(self):
        return self.speed

class TownCar(Car):

    __max_speed = 60

    def show_speed(self):
        msg = self.speed if self.speed < self.__max_speed else "превышение разрешенной скорости "+str(self.__max_speed)
        return msg


class SportCar(Car):
    pass

class WorkCar(Car):

    __max_speed = 40

    def show_speed(self):
        msg = f"Tекущая скорость {self.speed}" if self.speed < self.__max_speed else f"Tекущая скорость {self.speed} превышение разрешенной скорости {str(self.__max_speed)}"
        return msg


class PoliceCar(Car):
    def __init__(self, name, color, speed=0, is_police=True):
        super().__init__(name, color, speed, is_police)

def drive(car, speed_after_start, turn, speed_after_turn):
    print(50 * "-")
    print("Работаем с объектом класса ", car.__class__)
    print(f" Параметры машины название {car.name}, цвет {car.color}, скорость {car.speed}, полицейская {car.is_police}")
    print(car.name, car.go())
    car.speed = speed_after_start
    print(car.show_speed())
    print(car.name, car.turn(turn))
    car.speed = speed_after_turn
    print(car.show_speed())
    print(car.name, car.stop())

car1 = Car("Лада", "Баклажан")
drive(car1, 30, "налево", 80)

t_car1 = TownCar("Ford", "синий")
drive(t_car1, 30, "направо", 80)

w_car1 = WorkCar("Газель", "белый")
drive(w_car1, 30, "направо", 50)

p_car1 = PoliceCar("Буханка", "Зеленый")
drive(p_car1, 30, "через две сплошные", 150)
