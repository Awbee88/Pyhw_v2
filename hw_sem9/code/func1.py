# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


# day = int(input('Input number of day in week: '))


def day_of_week(day):
    if day in range(1, 8):
        if day == 6 or day == 7:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'Error'
