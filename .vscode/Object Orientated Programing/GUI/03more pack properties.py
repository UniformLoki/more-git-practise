from tkinter import *

window = Tk()

l1 = Label(window, text="a",bg="red", fg="white")
l1.pack(side= LEFT ,fill=X, expand=1)
l2 =Label(window,text="b",bg="green",fg="white")
l2.pack(side=LEFT,expand=1,fill=BOTH)
l3 =Label(window,text="c",bg="blue",fg="white")
l3.pack(side=LEFT,expand=1,fill=Y)

window.mainloop()