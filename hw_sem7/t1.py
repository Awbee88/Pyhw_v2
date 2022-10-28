"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time


class TrafficLight:

    def __init__(self):
        self.__color = 'Красный'

    def running(self):
        print(self.__color)
        for i in range(1, 8):
            print(i)
            time.sleep(1)
        self.__color = 'Желтый'
        print(self.__color)
        for j in range(1, 3):
            print(j)
            time.sleep(1)
        self.__color = 'Зеленый'
        print(self.__color)
        for k in range(1, 6):
            print(k)
            time.sleep(1)


light = TrafficLight()
TrafficLight.running(light)
