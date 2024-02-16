from tkinter import *
import PIL.Image
import PIL.ImageTk
from card_game import *

window = Tk()
window.geometry("450x485")
window["bg"] = "steelblue1"
window.title ="The Game Goes On FOREVER!"


img = PIL.Image.open("C:\Python Files\.vscode\more_python\card game\images\default.png")
img1 = img.resize((200,400))
img2 = PIL.ImageTk.PhotoImage(img1)
 
pic1=  Label(window, image = img2,bg="black")
pic1.grid(row = 1, column = 0,columnspan = 2, rowspan = 5,  pady = 5)

imga = PIL.Image.open("C:\Python Files\.vscode\more_python\card game\images\default.png")
imga1 = imga.resize((200,400))
imga2 = PIL.ImageTk.PhotoImage(imga1)
 
pic2 =Label(window, image = imga2,bg="black")
pic2.grid(row = 1, column = 4,columnspan = 2, rowspan = 5,  pady = 5)

compick = Label(window, text="Computer Picked", bg="dodgerblue",fg="white")
compick.grid(row =0,column=0, sticky=W)

yopick = Label(window,text="You Picked", bg="dodgerblue",fg="white")
yopick.grid(row =0,column=5)

def startgame():  
    pic1.destroy()
    pic2.destroy()
    g1 = Game()
    g1.Play()
    
def endgame():
    window.quit()
    
def reset_():

    img = PIL.Image.open("C:\Python Files\.vscode\more_python\card game\images\default.png")
    img1 = img.resize((200,400))
    img2 = PIL.ImageTk.PhotoImage(img1)
 
    pic1=  Label(window, image = img2,bg="black")
    pic1.grid(row = 1, column = 0,columnspan = 2, rowspan = 5,  pady = 5)

    imga = PIL.Image.open("C:\Python Files\.vscode\more_python\card game\images\default.png")
    imga1 = imga.resize((200,400))
    imga2 = PIL.ImageTk.PhotoImage(imga1)
 
    pic2 =Label(window, image = imga2,bg="black")
    pic2.grid(row = 1, column = 4,columnspan = 2, rowspan = 5,  pady = 5)

    
play = Button(window, text="Play", bg="dodgerblue",fg="white",command=startgame) 
play.grid(row=450,column=0,sticky =W)

restart = Button(window, text="restart", bg="dodgerblue",fg="white",command=reset_) 
restart.grid(row=450,column=0)

quit = Button(window, text="quit", bg="dodgerblue",fg="white",command=endgame) 
quit.grid(row=450,column=5,sticky=E)


class Game:# will read the deck list object to compare numbers and use the cards overloaded operators to decide a winner
    def __init__(self):
        self.deck = Deck().cards
        shuffle(self.deck)
        shuffle(self.deck)
        
    @property
    def deck(self):
        return self._deck
    @deck.setter
    def deck(self, value):
        self._deck = value
    
    def Play(self):
        if len(self.deck) >0:
            card1 = self.deck.pop(randint(0,(len(self.deck)-1)))
            card_pic1 = card1.imagefile
            
            card2 = self.deck.pop(randint(0,(len(self.deck)-1)))
            card_pic2 = card2.imagefile
            shuffle(self.deck)
            
            imag = PIL.Image.open(f"C:\Python Files\.vscode\more_python\card game\images\{card_pic1}")
            img1 = imag.resize((200,400))
            img2 = PIL.ImageTk.PhotoImage(img1)
            Label(window, image = img2).grid(row = 1, column = 4,
            columnspan = 1, rowspan = 2,  pady = 5,sticky=E)
            
            print(f"C:\Python Files\.vscode\more_python\card game\images\{card_pic1}")
            print(f"C:\Python Files\.vscode\more_python\card game\images\{card_pic2}")
            imag1 = PIL.Image.open(f"C:\Python Files\.vscode\more_python\card game\images\{card_pic2}")
            imga1 = imag1.resize((200,400))
            imga2 = PIL.ImageTk.PhotoImage(imga1)
            Label(window, image = imga2).grid(row = 1, column = 1,
            columnspan = 1, rowspan = 2,  pady = 5,sticky=E)
            
            
            
            if (card1.number > card2.number):
                result = "\t You Win!"
                
                
            elif (card1.number < card2.number):
                result ="\t I win!"
                
                
            else:
                result = "Guess its a draw."
            wol = Label(window, text=result, bg="steelblue1",fg="white")
            wol.grid(row=430,column=3,sticky=S + N+ E+ W)
                
        else:
            self.End()
    
    
    def End(self):
        print("sorry to see you go.")
        print("________remaining cards_________")
        print(Deck())

    



window.mainloop()


