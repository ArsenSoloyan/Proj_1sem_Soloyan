#Из исходного текстового файла (pazzl.html) выбрать все html-коды изображений.
#Посчитать их количество.

import re
p = re.compile(r"<td>(.*?)</td>", re.S)
g = []
count = 0
for i in open('pazzl.html.txt').read().split('\n'):
   if len(p.findall(i)) > 0:
      g.append(p.findall(i))
      count += 1

for i in g:
  print(*i)

print("Количество html-кодов изображений:", count)

