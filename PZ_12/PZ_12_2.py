#Даны два числа. Вывести порядковый номер меньшего из них.

from tkinter import *
def count_num(event):
    n1 = int(num1.get())
    n2 = int(num2.get())
    if n1 < n2:
        positive['text'] = "№1"
    if n2 < n1:
        positive['text'] = "№2"

root = Tk()
root.title("Поиск меньшего")
root.geometry("300x100")

Label(text="Первое число:").grid(row=1, column=0)
num1 = Entry()
num1.grid(row=1, column=1)

Label(text="Второе число:").grid(row=2, column=0)
num2 = Entry()
num2.grid(row=2, column=1)

button1 = Button(text="Найти")
button1.grid(row=4, column=1)

positive = Label()
positive.grid(row=5, column=1)

button1.bind('<Button-1>', count_num)

root.mainloop()