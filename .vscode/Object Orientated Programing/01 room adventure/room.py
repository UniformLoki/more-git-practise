from time import sleep

class Room:
    def __init__(self,name):
        self.name = name
        self.exit_directions = [] #forward backward
        self.exit_destinations = [] # the actual rooms
        self.items = []
        self.item_descriptions = []
        self.grabbables = []
        self.choice = []
        self.room_descriptions = []
        
        
    #getters/setters
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def exit_directions(self):
        return self._exit_directions
    
    @exit_directions.setter
    def exit_directions(self, direction):
        self._exit_directions = direction
        
    @property
    def exit_destinations(self):
        return self._exit_destinations
    
    @exit_destinations.setter
    def exit_destinations(self, place):
        self._exit_destinations = place
        
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, object):
        self._items = object
        
    @property
    def item_descriptions(self):
        return self._item_descriptions
    
    @item_descriptions.setter
    def item_descriptions(self, descrip):
        self._item_descriptions = descrip     
        
    @property
    def grabbables(self):
        return self._grabbables
    
    @grabbables.setter
    def grabbables(self, thing):
        self._grabbables = thing
        
    @property
    def choice(self):
        return self._choice
    
    @choice.setter
    def choice(self, yn):
        self._choice = yn
        
    @property
    def room_descriptions(self):
        return self._room_descriptions
    
    @room_descriptions.setter
    def room_descriptions(self, descrip):
        self._room_descriptions = descrip 
        
        
    # additional methods
    def add_exit(self, exit_direction, exit_destination):
        self.exit_directions.append(exit_direction)
        self.exit_destinations.append(exit_destination)
        
    def add_item(self, item_name, item_description):
        self.items.append(item_name)
        self.item_descriptions.append(item_description)
        
    def add_grabbable(self, new_grabbable):
        self.grabbables.append(new_grabbable)
        
    def delete_grabbable(self, existing_grabbable):
        if existing_grabbable in self.grabbables:
            self.grabbables.remove(existing_grabbable)
    
    def add_choice(self, yes_no):
        self.choice.append(yes_no)
    
            
    def __str__(self):
        
        result = ''
        
        # room name
        if self.name == "dark room":
            result += f"you awake in a {self.name}\n"
        else:
            result += f"you are in {self.name}\n"
        
        # exits
        if len(self.exit_directions) != 0:
            result += "Exits: \n"
            x = 0
            while x <= 2:
                item = self.items[x]
                result += f"{self.exit_directions[x]}: {item} "
                x += 1
        
        return result
        
