# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел.
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Содержимое первого файла:
# Отрицательные элементы:
# Количество отрицательных элементов:
# Среднее арифметическое:

# Содержимое второго файла:
# Положительные элементы:
# Количество положительных элементов:
# Сумма положительных элементов:
import random
print(', '.join(map(str, [random.randint(-9, 9) for i in range(random.randint(3, 12))])), file=open('file1.txt', 'w'))
print(', '.join(map(str, [random.randint(-9, 9) for o in range(random.randint(3, 12))])), file=open('file2.txt', 'w'))
u = open('new_file.txt', 'w')
c, d = [int(i) for i in open('file1.txt').read().split(', ')], [int(i) for i in open('file2.txt').read().split(', ')]
print('Содержимое первого файла:', open('file1.txt').read(), file=u)
print('Содержимое второго файла:', open('file2.txt').read(), file=u)
print('Отрицательные элементы:', [i for i in c if i < 0], '\n', file=u)
print('Положительные элементы:', [i for i in d if i > 0], '\n', file=u)
print('Количество отрицательных элементов:', len([i for i in c if i < 0]), '\n', file=u)
print('Количество положительных элементов:', len([i for i in d if i > 0]), '\n', file=u)
print('Среднее арифметическое первого файла:', sum(c) / len(c), '\n', file=u)
print('Сумма положительных элементов:', sum([i for i in d if i > 0]), '\n', file=u)
