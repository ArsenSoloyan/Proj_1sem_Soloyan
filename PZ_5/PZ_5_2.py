# Описать функция Power1(A,B) вещественного типа, находящую величину AB по
# формуле AB = exp(B*ln(A)) (параметры A и B - вещественные). В случае
# нулевого или отрицательного параметра A функция возвращает 0. С помощью
# этой функции найти степени A^P, B^P, C^P, если даны числа P,A,B,C.

import math


def power1(x, y):                              # функция, находящая степень числа
    if float(x) > 0:
        res = round(math.exp(float(y) * math.log(x)), 10)
        return res
    else:
        return 0


P = input("Введите число P (степень чисел): ")
while type(P) != float:         # обработка исключений
    try:
        P = float(P)
    except ValueError:
        print("Введите снова!")
        P = input("Введите степень числа: ")
A = input("Введите число A: ")
while type(A) != float:         # обработка исключений
    try:
        A = float(A)
    except ValueError:
        print("Введите снова!")
        A = input("Введите число: ")
B = input("Введите число B: ")
while type(B) != float:         # обработка исключений
    try:
        B = float(B)
    except ValueError:
        print("Введите снова!")
        B = input("Введите число: ")
C = input("Введите число C: ")
while type(C) != float:         # обработка исключений
    try:
        C = float(C)
    except ValueError:
        print("Введите снова!")
        C = input("Введите число: ")
print("A ^ P =", power1(A, P))
print("B ^ P =", power1(B, P))
print("C ^ P =", power1(C, P))