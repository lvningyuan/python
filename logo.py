from tkinter import *

root = Tk()

photo = PhotoImage(file='1.png')
Label(root, image=photo).pack()


def show():
    print('正中靶心')

Button(root,text='点我',command=show).place(relx=0.5,rely=0.5, anchor=CENTER)

mainloop()
