def sorter(numbs):
    for i in range(len(numbs)):
            for j in range(0,len(numbs)-i-1):
                if numbs[j] > numbs[j + 1]:
                    temp = numbs[j]
                    numbs[j] = numbs[j+1]
                    numbs[j+1] = temp
    return(numbs)

def list_adder(numbs):

    keep_going = input("would you like to add another number to the list(Y/N)?")
    if keep_going == "y":
        number = int(input("Please enter a integer."))
        numbs.append(number)
        list_adder(numbs)
    else:
        print(numbs)
        sorted = sorter(numbs)
        print(sorted)
 
numbs = []        
list_adder(numbs)
        
            