"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):

        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        if direction == 'налево':
            return 'Машина повернула налево'
        elif direction == 'направо':
            return 'Машина повернула направо'

    def show_speed(self):
        return f'Ваша скорость {self.speed} km/h'


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Осторожно, вы превысили допустимую скорость! {self.speed} km/h'
        else:
            return f'Ваша скорость {self.speed} km/h'


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Осторожно, вы превысили допустимую скорость! {self.speed} km/h'
        else:
            return f'Ваша скорость {self.speed} km/h'


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


my_town_car = TownCar(54, 'Серый', 'Kia', False)
my_sport_car = SportCar(123, 'Чёрный', 'Tesla', False)
my_work_car = WorkCar(45, 'Белый', 'ZIL', False)
my_police_car = PoliceCar(77, 'Синий', 'Ford', True)

print(my_town_car.name)
print(my_sport_car.color)
print(my_work_car.speed)
print(my_police_car.is_police)

print(my_work_car.show_speed())
print(my_sport_car.go())
print(my_police_car.turn('налево'))
print(my_town_car.show_speed())
