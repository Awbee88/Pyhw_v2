# Напишите функцию is_palindrome(text), 
# которая принимает в качестве аргумента строку text 
# и возвращает значение True если указанный текст 
# является палиндромом и False в противном случае.


def is_palindrome(s):
    lst = []
    for i in s.lower():
        if i.isalpha and i not in ' .,!?-':
            lst.append(i)

    if lst==lst[::-1]:
        return True
    else:
        return False