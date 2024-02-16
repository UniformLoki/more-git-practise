from random import choice, randint
from tkinter import *


width = 1000
height = 1000
Point_colors = (["black", "red", "green", "blue"])
Point_radius = 0
Num_points = 250000


class ChaosGame(Canvas):
    def __init__(self, parent): # parent is the container (the window)
        Canvas.__init__(self,parent,bg="white")
        self.pack(fill=BOTH,expand=1)
        
    def plot_all_points(self, num_points):
        v1 = [0,height-1]
        v2 = [(width-1)/2,1]
        v3 = [width -1, height-1]
        vertices = [v1,v2,v3]
        self.plot_point(v1[0], v1[1])
        self.plot_point(v2[0], v2[1])
        self.plot_point(v3[0], v3[1])
        
        p1 = choice(vertices)
        p2 = choice(vertices)
        
        mid = [ (p1[0]+p2[0])/2,(p1[1]+p2[1])/2 ]
        self.plot_point(mid[0],mid[1])
        
        for i in range(num_points):
            p1 = choice(vertices)
            new_mid = [ (p1[0]+mid[0])/2,(p1[1]+mid[1])/2 ]
            self.plot_point(new_mid[0], new_mid[1])
            mid = new_mid
    
    def plot_point(self,x0,y0):
        rand_color =choice(Point_colors)
        x1 = x0 + Point_radius*2
        y1 = y0 + Point_radius*2
        self.create_oval(x0,y0,x1,y1, outline =rand_color, fill=rand_color)
        
    
window = Tk()
window.geometry(f"{width}x{height}")
window.title("Points")
p = ChaosGame(window)

p.plot_all_points(Num_points)
window.mainloop()