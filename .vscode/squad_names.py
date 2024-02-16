#####################################################################
# author: Joseph Matherne
# date: 11/30/23
# description: This code takes the string items from a list and searches for a user specified substring within them
####################################################################

def file_reader(filename:str): #Takes file name from user and assignes it to a list while also ensure the name is correct
    my_file = open(filename, "r")
    data_list = []
    for item in my_file:
        lower_item = item.lower()
        new_data = lower_item.split("\n")
        data_list.append(new_data[0])
    try:
        length = len(data_list)
        print (f"There are {length} items in this file.")
        return data_list
    except:
        print("Looks like the name you entered doesnt exist, please try again.")
        filename = input("What file would you like to read? ")
        file_reader(filename)


def beginner(prefix:str, file:str):#check if a specified substrng exists at the begining of a index
    true_count = 0
    for item in file:
        if (item.startswith(prefix)):
            true_count += 1
    return true_count

def ending(suffix:str, file:str):# checks if a specified substring exists at the end of an index
    true_count = 0
    for item in file:
        if (item.endswith(suffix)):
            true_count += 1
    return true_count

def contains(fix:str, file:str):# checks if a substring exists anywhere within an index
    true_count = 0
    for item in file:
        if fix in item:
            true_count +=1
    return true_count


def printer(file:str, substring:str):#takes the substring and list and finds the number of occurences of a substring
    print("________________________________________________________")
    start_len = beginner(substring, file)
    print(f"This file has {start_len} items that begin with {substring}.")
    end_len = ending(substring, file)
    print(f"This file has {end_len} items that end with {substring}.")
    contain_len = contains(substring, file)
    print(f"This file has {contain_len} items that contain {substring}.")
    print("________________________________________________________")#prints out results
    

filename = input("What file would you like to read? ")
my_file = file_reader(filename)
substring = input("What substring would you like to look for? ")
printer(my_file, substring)
    