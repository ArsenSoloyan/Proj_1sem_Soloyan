# Дано целое положительное число. Вывести символы, изображающие цифры
# этого числа (в порядке справа налево)

a = input("Введите целое положительное число: ")

while type(a) != int: #обработка исключений
    try:
        a = int(a)
    except ValueError:
        a = input("Введите целое положительное число: ")
while type(a) != int:  #обработка исключений
    try:
        a = int(N)
    except ValueError:
        a = input("Введите целое положительное число: ")
while a <= 0:
        a = input("Введите целое положительное число: ")

P = str(a)
print("  ", ",".join(P[::-1]))
