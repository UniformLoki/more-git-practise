

TESTING = False # Change this to False if you want to proceed to the
# game itself. Leave it as True if you want to test
# the Card and Deck classes.
########## DO NOT CHANGE ANYTHING BELOW THIS LINE ##########
# import the CardGame file and all its classes.
import random
if (TESTING):
# Testing: the CARD class
    c1 = Card(2, "hearts")
    c2 = Card(4, "diamonds")
    print(f"{c1} > {c2}: {c1>c2}")
    print(f"{c1} < {c2}: {c1<c2}")
    print(f"{c1} == {c2}: {c1==c2}")
    print("-" * 40)
    c3 = Card(21, "uno")
    c4 = Card(-6, "queens")
    print(f"{c3} > {c4}: {c3>c4}")
    print(f"{c3} < {c4}: {c3<c4}")
    print(f"{c3} == {c4}: {c3==c4}")
    print("-" * 40)
    c5 = Card(1, "Diamonds")
    print(f"{c5} > {c2}: {c5>c2}")
    print(f"{c5} < {c2}: {c5<c2}")
    print(f"{c5} == {c2}: {c5==c2}")
    print("-" * 40)
# Testing: The Deck Class
    random.seed(1234)
    d1 = Deck()
    print(d1)
    print("-" * 40)
    d1.shuffle()
    d1.shuffle()
    print(d1)
    print("-" * 40)
    c6 = d1.draw()
    c7 = d1.draw()
    print(f"{c6} > {c7}: {c6>c7}")
    print(f"{c6} < {c7}: {c6<c7}")
    print(f"{c6} == {c7}: {c6==c7}")
    print("-" * 40)
    for i in range(32):
        c8 = d1.draw()
    print(f"c8 = {c8}")
    print(f"d1 = {d1}")
    c8 = d1.draw()
    c8 = d1.draw()
    print(f"c8 = {c8}")
    print(f"d1 = {d1}")
    c8 = d1.draw()
    c8 = d1.draw()
    print(f"c8 = {c8}")
    print(f"d1 = {d1}")
    print("-" * 40)
# Testing: The Game Class
else:
    g1 = Game()
    g1.start()

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
            card1 = self.deck[randint(0,(len(self.deck)-1))]
            card2 = self.deck[randint(0,(len(self.deck)-1))]
            shuffle(self.deck)
            print(f"You picked {card1}, and I picked {card2}")
            if (card1 > card2):
                print("\t You Win!")
                question = input("Would you like to play again? y/n")
                
            elif (card1 < card2):
                print("\t I win!")
                question = input("Would you like to play again? y/n")
                
            else:
                print("Guess its a draw.")
                question = input("Would you like to play again? y/n")
                
        else:
            print("Not enough cards to play.")
            self.End()
        if (question == "y"):
            self.Play()
        else:
            self.End()
    
    
    def End(self):
        print("sorry to see you go.")
        print("________remaining cards_________")
        print(Deck())
    
    def start(self):
        print("_" * 60)
        print("\t\twelcome to a basic game")
        print("You and this program will take turns puicking cards")
        print("The one with the highest value card wins")
        print("_"*60)
        inquiry = input("are you ready to start y/n?")
        if inquiry == "y":
            self.Play()
            
        else:
            self.End()