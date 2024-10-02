from tkinter import*
root = Tk()
root.geometry("300x300")

def fun_1():
   text_str1.config(text=root.geometry())

def fun_2():
   text_str1.config(text=input_1.get())

text_str1 = Label(text=root.geometry() , font="system 20" , bg="#a600a6" , fg="#ffffff")
text_str1.place(x=10, y=10)
but_1 = Button(text="click", command=fun_1)
but_1.place(x=50, y=50)

input_1 = Entry(width=10,fg="#ffffff")
input_1.place(x = 50, y=100)
but_2 = Button(text="text input", command=fun_2)
but_2.place(x=50, y=130)

text_str2 = Label(bg="#a600a6")
text_str2.place(x=200 , y = 200 , width= 20 , height=20)

root.mainloop()