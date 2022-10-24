"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
Пример:
1 2 3
4 5 6
7 8 9
1 2 3
4 5 6
7 8 9
Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()
        return ''

    def __add__(self, other):
        new_matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_matr[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return new_matr


my_matr1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_matr2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_matr1)
print(my_matr2)
my_matr3 = Matrix(my_matr1 + my_matr2)
print(my_matr3)
