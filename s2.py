# 14). Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

'''
fl_num = input('Введите вещественное число: ')
total = 0
for i in fl_num:
    if i.isdigit():
        total+= int(i)
print(total)
'''

# 15). Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

'''
try:
    n = int(input('Input your num: '))
    total = 1
    for i in range(1,n+1):
        print(total*i, end=' ')
        total*=i
except:
    print('Value Error')
'''

# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

'''
n = int(input('Input your num: '))
nums = []
for i in range(1, n+1):
    nums.append((1+1/i)**i)
print(sum(nums))
'''

# 17). 14. Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке)
# в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

'''
from random import randint
total = 1
n = int(input('Input your num: '))
nums = [i for i in range(-n, n+1)]

file = open('file.txt', 'w')
for _ in range(n):
    file.write(str(randint(0, n))+'\n')

print(nums)

file = open('file.txt', 'r')
for line in file:
    total *= nums[int(line)]
file.close()

print(total)
'''


# 18). Реализуйте алгоритм перемешивания списка.

'''
arr = ['234', '124', '2134', '5436', '3462', '1235']
new_arr = ['']*len(arr)

for i in range(len(new_arr)):
    ind = randint(0, len(arr)-1)
    new_arr[i] = arr[ind]
    del arr[ind]

print(new_arr)
'''
