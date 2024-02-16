#Formal Parameters vs Actual Parameters

# Formla parameters are the defined paramters
#    found in function header
#   -aka parameters

def average(a,b):# formal params a and b
    pass



# Actual Parameters are the values passed into the function
# when it is called
#  -aka arguments

average(1,2) # formal params 1 and 2

val1 = 10
val2 = 20
average(val1, val2)




def file_reader(filename):
    my_file = open(filename, "r")
    data = my_file.read()
    data_list = data.split("\n")
    try:
        length = my_file.len()
        print (f"There are {length} items in this file.")
        return data_list
    except:
        print("Looks like the name you entered doesnt exist, please try again.")
        filename = input("What file would you like to ead?")
        file_reader(filename)