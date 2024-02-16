####################################################################
# author: Joseph matherne
# date: 1/25/24
# description: this code will calculate the cost, price, and profit of item and ensure cost and price are not negative and takes new product types
#####################################################################

class Item:
    
    def __init__(self, name:str = "jorts" , cost:float=0 , price:float=0):# The SaleItem class has a name, cost and price. All three are provided
        
        self.price = price
        self.name = name
        self.cost = cost
        
        
    @property
    def cost(self):
        return self._cost
    
    @cost.setter# ensures value is never negative
    def cost(self, value):
        if value < 0:
           value = 0 
        self._cost = value
        
    @property# ensures value is never negative
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
           value = 0 
        self._price = value
        

        
    
    
    def applySale(self, percentoff:int = 0):# sets final price of item no matter what
            print(percentoff)
            realcost = (float(self.price) -  float(self.price * (percentoff/100)))
            
            self.price = realcost
        
    def profit(self): # calculates profit
            profit = float(self.price) - float(self.cost)
            return profit
        
    def __str__(self):
        output = ""
        output += f"{self.name}\t{self.cost:.2f}\t{self.price:.2f}"
        return output
    
    
class Clothing(Item):
    brand = ""
    size = 0
    def __init__(self, name, brand, cost,price,size):
        Item.__init__(self,name, cost, price)
        self.brand = brand
        self.size = size
        
    @property
    def size(self):
        return self._size
    
    @size.setter# ensures value is never negative
    def size(self, value):
        if value < 0:
           value = None 
        self._size = value
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter# ensures value is never negative
    def brand(self, name): 
        self._brand = name

    def __str__(self):
        output = ""
        output += f"{self.name}\t{self.cost:.2f}\t{self.price:.2f}"
        output += f" |{self.brand}  Size:{self.size}"
        
        return output
    
    
class Food(Item):
 
    def __init__(self,name,cost,price):
        Item.__init__(self,name, cost, price)
        self.shelfLife = 7
        if (self.shelfLife <0):
            self.shelfLife = None

    
    def __str__(self):
        output = ""
        output += f"{self.name}\t{self.cost:.2f}\t{self.price:.2f}"
        if self.shelfLife <0:
            self.shelfLife = None
        output+= f" |this product will expire in {self.shelfLife} days"
        return output
        
class Shoe(Clothing):
    def __init__(self, cost, price, size):
        Clothing.__init__(self, "Crocs" , "Nike" , cost, price, size)
       
   

class Chips(Food): 
    def __init__(self):
        Food.__init__(self, "Lays", 2, 3.50)
        self.shelfLife = 21
        if self.shelfLife <0:
            self.shelfLife = None
        
        





# Create 3 basic items and print them
i1 = Item("bananas", 2, 4.59)
i2 = Item("jeans", 30, 44.99)
i3 = Item("shirt", 20, 29.99)
print("Item\tCost\tPrice\tExtra Info")
print("-" * 50)
print(i1)
print(i2)
print(i3)
print("-" * 50)
# Create Clothing and Food items and print them
c1 = Clothing("jeans", "Levis", 30, 44.99, 32)
c2 = Clothing("shirt", "Macy's", 20, 29.99, 16)
f1 = Food("bananas", 2, 4.59)
f2 = Food("Avocado", 1.50, 5.50)
f2.shelfLife = 2
print(c1)
print(c2)
print(f1)
print(f2)
print("-" * 50)
# Create Shoes and Chips and print them
s1 = Shoe(59.99, 89.99, 10)
s2 = Shoe(49.99, 79.99, 4)
h1 = Chips()
print(s1)
print(s2)
print(h1)
print("-" * 50)
# Testing out the range checking
h1.shelfLife = -5
s2.size = -2
print(s2)
print(h1)
print("-" * 50)
