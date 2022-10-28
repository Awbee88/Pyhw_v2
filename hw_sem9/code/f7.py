# Напишите функцию с именем find_all(target, symbol), которая принимает
# два аргумента: строку target и символ symbol и возвращает список,
# содержащий все местоположения этого символа в строке.

def find_all(target, symbol):
    indx = []
    for i in range(len(target)):
        if target[i] == symbol:
            indx.append(i)
    return indx
