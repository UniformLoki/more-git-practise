#joseph matherne
#1/31/24
# the reckoner
from tkinter import *
from buttondata import button_data

width = 400
height = 650

class MainGUI(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self,parent,bg="white")
        # parent attributes("-fullscreen", True)
        self.setupGUI()
        self.clear = False
       
        
    def setupGUI(self):
        # the display is where it displays what we are typing
        self.display = Label(
            self,
            text="",
            anchor = E,
            bg="white",
            fg="black",
            height =1,
            font =("TexGyreAdventor", 50)  
        )
        self.display.grid(
            row=0,
            column= 0,
            columnspan=4,
            sticky=NSEW
        )
        for row in range(6):
            Grid.rowconfigure(self,row,weight=1)
        for col in range(4):
            Grid.columnconfigure(self,col,weight=1)
            
        for button in button_data:
            self.make_button(button["row"],button["column"], button["value"])
        self.pack(fill=BOTH,expand=1)
    
    def make_button(self,row,col,value):
        _columnspa = 1
        bg_color = "#dddddd"
        if value == "=":
            bg_color = "blue"
            _columnspa = 2
        if value in ["(",")","AC","**","+","-","*","/", "%","<-"]:
            bg_color ="#999999"
            
        button = Button(self,font = ("Comic Sans MS",30), text = value, fg = "black", bg = bg_color,highlightbackground = bg_color, borderwidth=0, highlightthickness=0, width=5,activebackground="white",command=lambda:self.process(value))

        button.grid(row=row,column=col,sticky=NSEW, columnspan = _columnspa)
    
    def clear_display(self):
        self.display["text"] = ""
    
    
    def set_display(self,value):
        self.display["text"] = value
        
    def append_display(self,value):
        self.display["text"] += value
    
    def evaluate(self):
        expr = self.display["text"]
        try:
            self.clear_display()
            result = str(eval(expr))
            if len(result)>= 14:
                result = result[0:11] + "..."
                self.set_display(result)
                self.clear = True
            else:
                self.set_display(result)
                self.clear = True
        except:
            self.set_display("ERROR")
        
            
    
    def process(self,button):
        if button == "AC":
            self.clear_display()
        elif button == "=":
            self.evaluate()
            lambda: self.clear_display()
        elif button == "<-":
            self.display["text"] = self.display["text"][0:-1]
            
        else:
            if self.display["text"] == "ERROR":
                self.clear_display()
            elif (len(self.display["text"]) >= 14):
                self.display["text"]
            elif self.clear == True:
                self.clear_display()
                self.append_display(button)
                self.clear = False
            else:
                self.append_display(button)
    
    
    
#main
window = Tk()
window.title("The Reckoner")
window.geometry(f"{width}x{height}")
p = MainGUI(window)
window.mainloop()

#assignment
#1 clear the display at all appropriate times
#   - just evalutated something

#2^n -1
#!0 = 1
#!1 = 1
#!2 = 2*!1
#!3 = 3*2*1

#   x       f(x)
#   0       1
#   1       1*f(0)
#   2       2*f(1)
#   3       3*f(2)
#   .       .
#   .       .
#   .       .
#   n       n*f(n-1)


#def a recurrence relation is a equation that is defined as a function of the preceeding terms
#def recurrsion is the process of a function clling itself until a base case is reached
# 2 parts: base case(s) and the recursive step
#(n)= n!
#(r)  r!(n-r)!

