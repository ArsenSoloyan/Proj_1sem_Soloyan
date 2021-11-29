# Дан список размера N и целые числа K и L (1 < K < L < N).
# Найти сумму всех элементов списка, кроме элементов с номерами от K до L включительно.

import random

N = int(input())
arr = []
k = int(input())
l = int(input())
for i in range(N):
    ran = random.randint(1,100)
    arr.append(ran)
    arr.sort()
print(arr)

for i in range(N):
    i += i
    if arr = [k] or arr =