# from tkinter import*
from tkinter import Tk,Label,Button

# https://metanit.com/python/tkinter/2.5.php
# https://metanit.com/python/tkinter/2.2.php

root = Tk()
root.geometry("600x500")
root.title("ouo")
# n: положение вверху по центру
# e: положение в правой части контейнера по центру
# s: положение внизу по центру
# w: положение в левой части контейнера по центру
# nw: положение в верхнем левом углу
# ne: положение в верхнем правом углу
# se: положение в нижнем правом углу
# sw: положение в нижнем левом углу
# center: положение центру
text = Label(text="hello")
text.place(relx=0.5, rely=0.5,anchor="center")
text_2 = Label(text="hello_2", bg="#9fee00")
text_2.place(x=100,y=100)
def run():
    text_2.config(text="ddd", bg="#a600a6")
    button_1.config(text="ddd", bg="#a600a6")


button_1 = Button(text="кнопка", command=run)
button_1.place(x=200,y=200)


root.mainloop()



# dz
# задача 1
# Создайте игру clicker, при нажатии на кнопку должно число увеличиваться на один

# задача 2
# Сделать игру найди кнопку, при нажатии на кнопку она перемещается в случайное место по координатам ,но не выходит за границы окна

