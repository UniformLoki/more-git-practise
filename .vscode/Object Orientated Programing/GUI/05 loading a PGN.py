from tkinter import *
import PIL.Image
import PIL.ImageTk

window = Tk()

pillow_image = PIL.Image.open("C:\Python Files\.vscode\more_python\card game\joker.png")
resized_image = pillow_image.resize((200,200))
photoimage = PIL.ImageTk.PhotoImage(resized_image)

label = Label(window, image=photoimage)
label.grid()

window.mainloop()