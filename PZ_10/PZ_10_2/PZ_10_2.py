# Из предложенного текстового файла (text18-21.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст в
# стихотворной форме выведя строки в обратном порядке.
print(open('text18-21.txt').read() + str(len([i for i in open('text18-21.txt').read() if i in '.,?!:;'])))
print(open('text18-21.txt').readlines()[-1] + open('text18-21.txt').readlines()[-2] +
      open('text18-21.txt').readlines()[-3] + open('text18-21.txt').readlines()[-4] +
      open('text18-21.txt').readlines()[-5] + open('text18-21.txt').readlines()[-6] +
      open('text18-21.txt').readlines()[-7], file=open('new_file18_21.txt', 'w'))
