from room import Room
from time import sleep

class Game:
    
    def __init__(self):
        self.inventory = []
        self.current_room = None
        self.response = ""
        self.running = True
        self.create_rooms()
    
    
    def create_rooms(self):# create the rooms
        r1 = Room("dark room")
        r2 = Room("Hallway")
        rs = Room("the_long_fall")
        r3 = Room("Hallway")
        r4 = Room("Hallway")
        r5 = Room("Hallway")
        r6 = Room("Void")
        rd = Room("devroom")
        r7 = Room("The_end")
        rw = Room("window")
        # add exits
        r1.add_exit("door", r2)
        r1.add_exit("window", rs)
        r1.add_exit("sleep", r6)
        
        r2.add_exit("forward", r3)
        r2.add_exit("backward", r2)
        r2.add_exit("window", rw)
        
        r3.add_exit("forward", r4)
        r3.add_exit("backward", r2)
        r3.add_exit("window", rw)
        
        r4.add_exit("forward", r5)
        r4.add_exit("backward", rd)
        r4.add_exit("window", rw)
        
        r5.add_exit("forward", r6)
        r5.add_exit("backward", r7)
        r5.add_exit("window", rw)
        
        r6.add_exit("theres", r7)
        r6.add_exit("no", r7)
        r6.add_exit("escape", r7)
        
        #add items
        r1.add_item("the hallway emits a sterile orange glow\n", " ")
        r1.add_item("the window shows an endless see of bleak grey, only descernable by color as the dim light illuminates your skin \n", "your not supposed to see this")
        r1.add_item("you close your eyes and let your body melt into the floor", " ")
        
        r2.add_item("the solid long tube lamp above you give you two solid shadows on either side\n", " ")
        r2.add_item("as you try to go back you can't seem to find the room you awoke in\n", " ")
        r2.add_item("as you step towards the window an unseen hand pushes you through", " ")
        
        r3.add_item("your shadow has been growing consistently darker as you walk\n", " ")
        r3.add_item("you still can't find that room you awoke in\n", " ")
        r3.add_item("on the other side of the window sits a golden meddow of sunflowers, you can't help but want to hop out into that sunshine", " ")
        
        r4.add_item("the light has started blinking every few steps, your shadows appear to lag behind in the receading darkness\n", " ")
        r4.add_item("if you want to go back so bad, hows about a secret ending? :] <3\n", " ")
        r4.add_item("the window pulls itself out of the wall and jumps onto you from above", " ")
        
        r5.add_item("the light has been out for a couple minutes now, wonder where your shadow ran off to\n", " ")
        r5.add_item("it all ends the same\n", " ")
        r5.add_item("just quit", " ")
        
        r6.add_item("So long\n", " ")
        r6.add_item("and thanks for\n", " ")
        r6.add_item("all the fish", " ")
        
        rw.add_item("quit\n", " ")
        rw.add_item("quit\n", " ")
        rw.add_item("quit", " ")
        
        #add grabblbles

        
        #add choices
        
        
        
        self.current_room = r1
    
    
    def handle_go(self, room):
        self.response = "invalid Exit"
        result = ""
        if room in self.current_room.exit_directions:
            index = self.current_room.exit_directions.index(room)
            self.current_room = self.current_room.exit_destinations[index]
            self.response = "room changed"
            
            if len(self.current_room.exit_directions) != 0:
                result = "Exits: \n"
                x = 0
                while x <= 2:
                    item = self.current_room.items[x]
                    result += f"{self.current_room.exit_directions[x]}: {item} "
                    x += 1
        else:
            self.running == False
        
        self.response = result 
    
    def handle_look(self, noun):
        self.response = "invalid item"
        if noun in self.current_room.items:
            index = self.current_room.items.index(noun)
            self.responce = self.current_room.item_descriptions[index]
    
    def handle_take(self, item):
        self.response = "Invalid grabbable"
        if item in self.current_room.grabbables:
            self.inventory.append(item)
            self.current_room.delete_grabbable(item)
            self.response = f"Grabbed {item}"
            
        
    
    def play(self):

        while self.running:
        
            
            
            
            self.response = "invalid input, Try the format, [verb] [noun]"
            
            action = input("What would you like to do? ").lower()
            words = action.split()
            if len(words) == 2:
                verb = words[0]
                noun = words[1]
            
                if ((action in ["quit", "bye", "q", "exit"]) or (noun in ["quit", "bye", "q", "exit"])) :
                    self.running = False
                    break
                if (noun in ["the_long_fall","window", "The_end"] ):
                    self.death()
                    break
            
                if (noun in "devroom"):
                    self.devdeath()
                    break
                
                if verb == "go":
                    self.handle_go(noun)
                if verb == "look":
                    self.handle_look(noun)
                if verb == "take":
                    self.handle_take(noun)
                    
            print(self.response)
            sleep(1)

    
    def death(self):
        italic = "\033[3m"
        bold = "\033[1m"
        color = "\033[35m"
        reset = "\033[0m"
        print("the cold takes you" + italic + reset)
        self.running = False
    
    def devdeath(self):
        italic = "\033[3m"
        bold = "\033[1m"
        color = "\033[35m"
        reset = "\033[0m"
        print("your not supposed to be here, bye-bye" + italic + reset)
        self.running = False
        
        

    
    
