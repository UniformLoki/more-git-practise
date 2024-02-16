from tkinter import *


label1_style ={
    "bg":"red",
    "fg":"white"
}

label2_style ={
    "bg":"green",
    "fg":"white"
}


label3_style ={
    "bg":"blue",
    "fg":"white"
}


window = Tk()
#unpack the dictionary as keyword arguments (kwargs)
l1 = Label(window, text="a", **label1_style)
l1.pack(side= LEFT ,fill=X, expand=1)
l2 =Label(window,text="b",**label2_style)
l2.pack(side=RIGHT,expand=1,fill=BOTH)
l3 =Label(window,text="c",**label3_style)
l3.pack(side=LEFT,expand=1,fill=Y)

window.mainloop()