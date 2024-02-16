from tkinter import *

#create object refrence for the window

window = Tk()

#create label widget
text = Label(window, text='this is my gui')

#must manage the geometry of the element to get it to appear
#one way is with pack()
text.pack()

window.mainloop()