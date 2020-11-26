# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix():
    def __init__(self, list_lists):
        self.m_list = list_lists

    def __str__(self):
        m_view = ""
        for el in self.m_list:
            m_view = m_view + str(el)[1:-1].replace(',','') + '\n'
        return m_view

    def __add__(self, other):
        j=0
        temp_list = self.m_list
        self.m_list = []
        while j < len(other.m_list):
            self.m_list.append([sum(i) for i in zip(temp_list[j], other.m_list[j])])
            j +=1
        return self


mx_1 = Matrix([[31, 37, 51], [22, 43, 86], [17, 25, 21]])
mx_2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
mx_3 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
mx_4 = mx_1 + mx_2 + mx_3

print(mx_4)