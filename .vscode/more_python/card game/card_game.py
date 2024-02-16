#NAME: Joseph Matherne
#DATE: 1/31/24
#Purpose: this program will run a simple numbers matching game
import os.path

from random import seed,shuffle, randint
randseed = seed(9876543210)
POSSIBLESUITS = ["clubs", "diamonds", "hearts", "spades"]


class Card:# will create all card classes used
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    @property
    def number(self):
        return (self._number)
    @number.setter
    def number(self, value):
        if (value > 11) or (value <1):
            self._number = 2
        else:
            self._number = value
            
    @property
    def suit(self):
        return self._suit 
        
    @suit.setter
    def suit(self, type):
        if type not in POSSIBLESUITS:
            self._suit = "clubs"
        else:
            self._suit = type
            
    def __eq__(self, other_card):
        if (self.number == other_card.number):
            return True
        else:
            return False
        
    def __gt__(self, other_card):
        if (self.number > other_card.number):
            return True
        else:
            return False
        
    def __lt__(self, other_card):
        if (self.number < other_card.number):
            return True
        else:
            return False
        
    def __str__(self):
        statement = ""
        statement += f"{self.number} of {self.suit}"
        return statement
    
class Deck:# will compile all cards into a single list object
    def __init__(self):
        self.cards = []
        for number in range(2,11):
            for type in POSSIBLESUITS:
                self.cards.append(PictureCard(number, type))
    @property
    def cards(self):
        return self._cards
        
    @cards.setter
    def cards(self, new_card):
        self._cards = new_card            
    
    def shuffle(self):
        shuffle(self.cards)
        
    
    def Size(self):
        return len(self.cards)
    
    def draw(self):
        if len(self.cards)>0:
            drawn_card = self.cards.pop(0)
        else:
            drawn_card = None
        return drawn_card
    
    def __str__(self):
        output = ""
        if (len(self.cards)>0):
            for item in self.cards:
                output += f"{item}, "
               
        else:
            output+= "[--empty--]"
            
        return output
                
class PictureCard:
    def __init__(self, number, suit):
        Card.__init__(self, number, suit)
        self.number = number
        self.suit = suit
        self.imagefile = f"{self.number}_of_{self.suit}.png"
        
        
    @property
    def imagefile(self):
        return self._imagefile
    @imagefile.setter
    def imagefile(self, path):
        try:
            os.path.isfile(f"{path}")
            self._imagefile = path
        except:
            self._imagefile = "default.png"