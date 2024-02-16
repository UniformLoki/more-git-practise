####################################################################
# author: Joseph Matherne
# date: 11/07/23
# description:This code takes item names and prices and calculates total costs for specified items
######################### MAIN #####################################
####################################################################

def header():# print out the introduction
    print('Welcome to cyber groceries')
    print("________________________________")
    
def how_many():
    amount = int(input("How many items does the store carry"))
    return amount

def items(amount):# Prompt the user for the appropriate information
    x = 0
    groceries = []
    while (x < amount):
        x+=1
        item = input(f"What is the name of item #{x}\t")
        groceries.append(item)
    return groceries
        
def prices(groceries):# Prompt the user for the appropriate information
    x = 0
    costs = []
    while x < len(groceries):
        
        price = float(input(f"What is the price of {groceries[x]}\t"))
        x+=1
        costs.append(price)
    return costs
        
def quantity(groceries):# Prompt the user for the appropriate information
    x = 0
    amounts = []
    while x < len(groceries):
        amount = int(input(f"How many {groceries[x]} were bought today?\t"))
        x+=1
        amounts.append(amount)
    return (amounts)

def table(groceries, costs, amounts):# Print out items and their costs.
    x = 0
    print ("_____________________________________________")
    print ("Item \t Unit Price \t Number\t Total Cost")
    while x < len(groceries):
        total = (amounts[x]*costs[x])
        print(f"{groceries[x]} \t ${costs[x]} \t\t {amounts[x]} \t ${round(total,2)}\n")
        x+=1
        
header()
amount = how_many()
groceries = items(amount)
costs = prices(groceries)
amounts = quantity(groceries)
table(groceries,costs,amounts)