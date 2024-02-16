import requests
from tkinter import *
import PIL.Image
import PIL.ImageTk
import io

window = Tk()

response = requests.get(url="https://dog.ceo/api/breeds/image/random")

data = response.json()

response2 = requests.get(url=data["message"], stream=True)

pillow_image = PIL.Image.open(io.BytesIO(response2.content))
photoimage = PIL.ImageTk.PhotoImage(pillow_image)
label = Label(window, image=photoimage)
label.pack()

window.mainloop()