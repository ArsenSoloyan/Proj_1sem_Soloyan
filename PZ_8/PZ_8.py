# Дана строка "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4".
# Преобразовать информацию из строки в словарь, найти среднее арифметическое
# оценок, результаты вывести на экран.

student = {}
inf2 = 'Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4'.split()
student['Фамилия'] = inf2[0]  #преобразуем строки в словарь
student['Имя'] = inf2[1]
student['Группа'] = inf2[2]
student['Оценки'] = []
a = []
for i in inf2[3:]:
    b = student['Оценки'].append(int(i))
    a.append(int(i))
print("Получившийся словарь: ", student)
print("Среднее арифметическое оценок: ", sum(a) / len(a)) # находим среднее арифметическое
