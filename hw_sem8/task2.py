"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def cost(self):
        pass


class Clothes(AbstractClass):

    def __init__(self, vh, type):
        self.vh = vh
        self.__type = type

    @property
    def my_type(self):
        return self.__type

    @my_type.setter
    def my_type(self, value):
        self.__type = value


    def cost(self, type):
        if type == 'Пальто':
            return round(self.vh / 6.5 + 0.5, 2)
        if type == 'Костюм':
            return round(self.vh * 2 + 0.3, 2)

    @classmethod
    def total_cost(cls, cl1, cl2):
        return f'Общий расход ткани = {cl1 + cl2}'


cloth1 = Clothes(1.5, 'Пальто')
cloth2 = Clothes(1.3, 'Костюм')
print(f'Расход ткани на {cloth1.my_type} = {cloth1.cost(cloth1.my_type)}')
print(f'Расход ткани на {cloth2.my_type} = {cloth2.cost(cloth2.my_type)}')
print(Clothes.total_cost(cloth1.cost(cloth1.my_type), cloth2.cost(cloth2.my_type)))
