# Scope - the region of code that a variable is accessible in

#Global variables are accessible everywhere

a = 10



#Local variables are defined only within a region 0f the code

def my_func():
    a = 11
    print(f"Inside function: {a}")
    
print(f"Outside function: {a}")
my_func()



b = 20

def my_otherfunc():
    global b
    b += 3
    print(f"Inside: {b}")
    
print(f"Outside: {b}")
my_otherfunc()