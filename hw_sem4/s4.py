import random
from math import pi
from decimal import ROUND_FLOOR, ROUND_HALF_DOWN, Decimal
from re import I


# 30). Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10^(-1)≤d≤10^(-10)

'''
d = input('Введите точность для числа Пи(Пример: \'0.001\'): ')
def precision_pi(d):
    p = Decimal(pi)
    p = p.quantize(Decimal(d), ROUND_FLOOR)
    print(p)
precision_pi(d)
'''


# 31). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7]
# 140 = 2*2*5*7 => [2, 2, 5, 7]
# 140|2
# 70|2
# 35|5
# 7|7

'''
n = int(input('Input your number: '))
nums = []
d = 2
while n!= 1:
    if n%d == 0:
        nums.append(d)
        n//= d
    else: 
        d+=1

print(f'Список простых множителей введённого числа => {nums}')
'''


# 32). Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Первый вариант решения:
'''
num_list =[1, 5, 6, 75, 34, 3, 1, 1, 5, 3, 3, 5]
new_list = []

for i in num_list:
    if num_list.count(i)==1:
        new_list.append(i)
print(new_list)
'''

# Второй вариант решения:

'''
num_list =[1, 5, 6, 75, 34, 3, 1, 1, 5, 3, 3, 5]
num_set = set(num_list)
print(num_set)
'''


# 33). Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0

'''
def poly_to_file(k, file_name):

    polynomial = ''

    while k > -1:
        if k > 1:
            polynomial += str(random.randint(0, 100)) + '*x^' + str(k) + ' + '
            k -= 1
        elif k == 1:
            polynomial += str(random.randint(0, 100)) + '*x' + ' + '
            k -= 1
        elif k == 0:
            polynomial += str(random.randint(0, 100)) + ' = 0'
            k -= 1

    with open(file_name, 'w') as file:
        file.write(polynomial)

k = int(input('Введите степень многочлена: '))
poly_to_file(k, 'poly2.txt')
'''


# 34). Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).
# Пример:
# 1 Файл : 2*x2 + 4*x + 5 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
# Пример:
# 1 Файл : 2*x3 + 4*x2 + 5*x + 1 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 2*x3 + 8*x2 + 12

with open('poly1.txt', 'r') as file1:
    poly1 = file1.read()
with open('poly2.txt', 'r') as file2:
    poly2 = file2.read()

poly1_list = poly1.split(' = 0')
poly1_list = poly1_list[0].split(' + ')
print(poly1_list)
poly2_list = poly2.split(' = 0')
poly2_list = poly2_list[0].split(' + ')
print(poly2_list)
new_poly_list = []


if len(poly1_list) > len(poly2_list):
    for i in poly1_list:
        for j in poly2_list:
            if '^' in i and '^' in j:
                if i[i.find('^')+1:] == j[j.find('^')+1:]:
                    new_poly_list.append(
                        str(int(i[:i.find('*')])+int(j[:j.find('*')])) + i[i.find('*'):])
                elif i[i.find('^')+1:] != j[j.find('^')+1:] and i not in new_poly_list:
                    new_poly_list.append(i)
            elif ('x' in i and '^' not in i) and ('x' in j and '^' not in j):
                new_poly_list.append(str(int(i[:i.find('*')])+int(j[:j.find('*')])) + i[i.find('*'):])
            elif 'x' not in i and 'x' not in j:
                new_poly_list.append(str(int(i)+int(j)))
else:
    for i in poly2_list:
        for j in poly1_list:
            if '^' in i and '^' in j:
                if i[i.find('^')+1:] == j[j.find('^')+1:]:
                    new_poly_list.append(
                        str(int(i[:i.find('*')])+int(j[:j.find('*')])) + i[i.find('*'):])
                elif i[i.find('^')+1:] != j[j.find('^')+1:] and i not in new_poly_list:
                    new_poly_list.append(i)
            elif ('x' in i and '^' not in i) and ('x' in j and '^' not in j):
                new_poly_list.append(str(int(i[:i.find('*')])+int(j[:j.find('*')])) + i[i.find('*'):])
            elif 'x' not in i and 'x' not in j:
                new_poly_list.append(str(int(i)+int(j)))

with open('poly3.txt', 'w') as file3:
    new_poly = ' + '.join(new_poly_list) + ' = 0'
    file3.write(new_poly)
print(new_poly)

