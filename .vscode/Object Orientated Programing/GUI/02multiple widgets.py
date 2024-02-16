from tkinter import *

window = Tk()

l1 = Label(window, text="a",bg="red", fg="white")
l1.pack(fill=X)
l2 =Label(window,text="b",bg="green",fg="white")
l2.pack(fill=X)
l3 =Label(window,text="c",bg="blue",fg="white")
l3.pack(fill=Y)

window.mainloop()