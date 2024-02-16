def counter():
    x = 1
    numbers = []
    while x <= 1000000:
        numbers.append(str(x))
    return numbers

def x_checker(numbers):
    for item in numbers:
        if "0" in 