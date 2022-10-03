# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

'''
nums = [1, 35, 56, 4, 2, 7]
total = 0
for i in range(1,len(nums), 2):
    total += nums[i]
print(total)
'''

# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

'''
nums = [2, 3, 4, 5, 6]
product_arr = []
if len(nums)%2 == 1:
    for i in range(len(nums)//2+1):
        product_arr.append(nums[i]*nums[-i - 1])
else:
    for i in range(len(nums)//2):
        product_arr.append(nums[i]*nums[-i - 1])
print(product_arr)
'''
#  Или второй вариант задачи:

'''
a = [2, 3, 4, 5, 6]
b = []
c = -(-len(a)//2)
for i in range(c):
    b.append(a[i]*a[-1-i])
print(b)
'''

# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

'''
nums = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(len(nums)):
    nums[i] = nums[i] - round(nums[i])
if 0 in nums:
    nums.remove(0)
print(round(max(nums)-min(nums), 2))
'''

# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

'''
try:
    n = int(input('Input decimal number: '))
    a = []
    while n != 0:
        a.append(n % 2)
        n //= 2
    for i in a:
        print(i, end='')
except:
    print('Error!')
'''

# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Input your number: '))
a = 0
b = 1
fibo1 = [0]
for i in range(n):
    a,b = b, a+b
    fibo1.append(a)   
a = 0
b = 1
fibo2 = []
for i in range(n):
    a,b = b, a-b
    fibo2.append(a)
fibo2.reverse()
print(fibo2 + fibo1)

