

class Descript:

    def __set__(self, instance, value):
        if not 0 < value < 8:
            raise ValueError('Номер дня недели может быть в диапазоне от 1 до 7')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Descript2:

    def __set__(self, instance, value):
        if not 0 < value < 12:
            raise ValueError('Номер месяца может быть в диапазоне от 1 до 12')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Descript3:
    def __set__(self, instance, value):
        if not 0 < value < 32:
            raise ValueError('Номер дня в месяце может быть в диапазоне от 1 до 31')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Times:

    days_week = Descript()
    month = Descript2()
    days_month = Descript3()

    def __init__(self, days_week, days_month, month):
        self.days_week = days_week
        self.month = month
        self.days_month = days_month


var1 = Times(1, 20, 13)
var2 = Times(4, 38, 10)
var3 = Times(12, 15, 5)
print(var1)
print(var2)
print(var3)
