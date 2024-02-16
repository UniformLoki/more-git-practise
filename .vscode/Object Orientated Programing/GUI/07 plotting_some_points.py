from random import choice, randint
from tkinter import *


width = 400
height = 400
Point_colors = (["black", "red", "green", "blue"])
Point_radius = 0
Num_points = 2500


class CoordinatePlan(Canvas):
    def __init__(self, parent): # parent is the container (the window)
        Canvas.__init__(self,parent,bg="white")
        self.pack(fill=BOTH,expand=1)
        
    def plot_all_points(self, num_points):
        for _ in range(num_points):
            x = randint(0, width-1)
            y = randint(0,height-1)
            self.plot_point(x,y)
    
    def plot_point(self,x0,y0):
        rand_color =choice(Point_colors)
        x1 = x0 + Point_radius*2
        y1 = y0 + Point_radius*2
        self.create_oval(x0,y0,x1,y1, outline =rand_color, fill=rand_color)
        
    
window = Tk()
window.geometry(f"{width}x{height}")
window.title("Points")
p = CoordinatePlan(window)

p.plot_all_points(Num_points)
window.mainloop()