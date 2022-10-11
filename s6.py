# Выполнить математическое выражение, представленное в виде строки "(1+2)*3"


from re import X


text = "(13+2)*3"

'''
def parse(s):
    res = []
    digit = ''
    for el in s:
        if el.isdigit():
            digit += el
        elif el in ['(', ')']:
            if digit:
                res.append(float(digit))
                digit = ''
            res.append(el)
        else:
            if digit:
                res.append(float(digit))
                digit = ''
            res.append(el)
    else:
        if digit:
            res.append(float(digit))
    return res


def calc(lst):
    res = 0.0
    while '*' in lst:
        index = lst.index('*')
        res = lst[index-1] * lst[index+1]
        lst = lst[:index-1] + [res] + lst[index+2:]
    while '/' in lst:
        index = lst.index('/')
        res = lst[index - 1] / lst[index + 1]
        lst = lst[:index-1] + [res] + lst[index+2:]
    while '+' in lst:
        index = lst.index('+')
        res = lst[index-1] + lst[index+1]
        lst = lst[:index-1] + [res] + lst[index+2:]
    while '-' in lst:
        index = lst.index('-')
        res = lst[index-1] - lst[index+1]
        lst = lst[:index-1] + [res] + lst[index+2:]
    return res


def brackets(lst):
    while '(' in lst:
        open = lst.index('(')
        close = lst.index(')')
        lst = lst[:open] + [calc(lst[open + 1:close])] + lst[close+1:]
    return lst


print(parse(text))
result = parse(text)
result = brackets(result)
print(calc(result))
'''

# Улучшенная версия
'''
def parse(s):
    res = []
    digit = ''
    for el in s:
        if el.isdigit():
            digit += el
        elif el in ['(', ')']:
            if digit:
                res.append(float(digit))
                digit = ''
            res.append(el)
        else:
            if digit:
                res.append(float(digit))
                digit = ''
            res.append(el)
    if digit:
        res.append(float(digit))
    return res

def op(what, lst):
    while what in lst:
        index = lst.index(what)
        if what == '*':
            res = lst[index-1] * lst[index+1]
        elif what == '/':
            res = lst[index-1] / lst[index+1]
        elif what == '+':
            res = lst[index-1] + lst[index+1]
        elif what == '-':
            res = lst[index-1] - lst[index+1]
        lst = lst[:index-1] + [res] + lst[index+2:]
    return res, lst

def calc(lst):
    res = 0.0
    if '*' in lst: res, lst = op('*', lst)
    elif '/' in lst: res, lst = op('/', lst)
    elif '+' in lst: res, lst = op('+', lst)
    elif '-' in lst: res, lst = op('-', lst)
    return res

def brackets(lst):
    while '(' in lst:
        open = lst.index('(')
        close = lst.index(')')
        lst = lst[:open] + [calc(lst[open + 1:close])] + lst[close+1:]
    return lst

print(parse(text))
result = parse(text)
result = brackets(result)
print(calc(result))
'''

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

# 2 вариант
'''
nums = [1, 35, 56, 4, 2, 7]
print(sum(list(filter(lambda x: nums.index(x)%2, nums))))
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

# 2 Вариант

nums = [2, 3, 4, 5, 7]
print([nums[i]*nums[-i-1] for i in range(-(-len(nums)//2))])

