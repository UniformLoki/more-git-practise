####################################################################
# author: Joseph Matherne
# date:10/29
# description: This code will compile user inputs into two lists and pull from those lists to create an output
######################### MAIN #####################################
# In the space below, use the functions defined above to solve the
# outlined problem.
####################################################################
def intro():# print out the introduction
    print("-----------------------------------------------")
    print("Welcome to Cyber Groceries\t")
    print("-----------------------------------------------")

def how_many():# Prompt the user for the appropriate information
    amount = int(input("How mnay items is the customer buying?\t"))
    return(amount)

def grocery_write(amount):
    grocery_list = []
    x = 0
    while (x!= amount):
        x +=1
        item = input(f"What is item number {x}?\t")
        grocery_list.append(item)
    return(grocery_list)

def price_list(amount, grocery_list):
    cost_list = []
    x = 0
    y = 0
    while(x != amount):
        x +=1
        cost = float(input(f"What is the price of {grocery_list[y]}? \t"))
        y += 1
        cost_list.append(cost)
    return(cost_list)

def get_low(prices:list):# Figure out what the cheapest and most expensive items are as well as
    lowest_price = min(prices)
    low_index = prices.index(lowest_price)
    return low_index

def get_high(prices:list):# Figure out what the cheapest and most expensive items are as well as
    highest_price = max(prices)
    high_index = prices.index(highest_price)
    return high_index
            

def total(price):# what the total cost would be.
    total = sum(price)
    return(total)
    

intro()
number = how_many()
groclist = grocery_write(number)
prices = price_list(number, groclist)
cheapest  = groclist[get_low(prices)]
expensive = groclist[get_high(prices)]
totality = total(prices)
print("-----------------------------------------------")
print("Groceries = " + str(groclist))# Print out items and their costs.
print("Prices = " + str(prices))# Print out items and their costs.
print("-----------------------------------------------")
print(f"The cheapest item is {cheapest}")# Print out the information on cheapest, most expensive and total cost.
print(f"The most expensive item is {expensive}")# Print out the information on cheapest, most expensive and total cost.
print (f"Your total is {totality}")# Print out the information on cheapest, most expensive and total cost.
        