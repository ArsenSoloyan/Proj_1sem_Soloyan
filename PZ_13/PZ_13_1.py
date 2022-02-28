#Даны две последовательности. Найти элементы, различные для двух
#последовательностей и их среднее арифметическое.
from random import randint
from statistics import mean
n = [12, 19, 5, 40, 51]
g = [100, 12, 5, 50, 42]
p = list(set(n).difference(set(g)).union(set(g).difference(set(n))))
print(n, '\n' + str(g), '\n' + str(mean(p)))
