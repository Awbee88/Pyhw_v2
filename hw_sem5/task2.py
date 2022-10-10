# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

from random import randint

candy = 2021
player1 = 'Игрок 1'
player2 = 'Игрок 2'


def who_first():
    rand_num = randint(1, 2)
    if rand_num == 1:
        return 1, 'Игрок 1 ходит первым\n'
    elif rand_num == 2:
        return 2, 'Игрок 2 ходит первым\n'


def move(player):
    global candy
    flag = False
    print(f'{player} делает свой ход!')
    while not flag:
        try:
            total = int(input('Сколько конфет вы хотите забрать? \n'))
            if 0 < total < 29:
                flag = True
            else:
                print('Можно забрать только от 1 до 28 конфет!')
                flag = False
        except ValueError:
            print('Это не число! Введите пожалуйста целое число.')

    candy -= total
    print(f'{player} забирает {total} конфет и на столе остаётся {candy} конфет\n')
    if candy == 0:
        print(f'{player} выйграл! Ты молодец, можешь забрать себе все конфеты!')


temp = who_first()
if temp[0] == 1:
    print(temp[1])
    move(player1)
    while candy > 1:
        move(player2)
        move(player1)
elif temp[0] == 2:
    print(temp[1])
    move(player2)
    while candy > 1:
        move(player1)
        move(player2)


