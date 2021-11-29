# Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE, если не является — вывести FALSE

N = input("Введите целое положительное число: ")
while type(N) != int:                   # обработка исключений
    try:
        N = int(N)
    except ValueError:
        N = input("Введите целое положительное число: ")
while N <= 0:                           # обработка исключений
    N = input("Введите целое положительное число: ")
    while type(N) != int:
        try:
            N = int(N)
        except ValueError:
            N = input("Введите целое положительное число: ")

while N % 3 == 0:
    N = N / 3
print("Является степенью 3: ", N == 1)