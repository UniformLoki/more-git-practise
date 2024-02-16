def num_pairs(num_people):
    #base case
    if num_people == 1:
        return 0
    else:
        return ((num_people-1) + num_pairs(num_people -1))
    
    
def factorial(x):
    if x ==0:
        return 1
    
    else:
        return(x * factorial(x-1))
    

def pow(x,n):
    if n == 0:
        return 1
    else:
        return (x*pow(x,n-1))
    
    
def fib(n):
    if n ==1:
        return 0
    elif n ==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))