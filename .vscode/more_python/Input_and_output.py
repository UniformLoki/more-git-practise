val = input("Give me a value: ")
a_number = int(input("Give me an integer: ")) # casting

#output
print("Hellow World")
print("Hello", end="")#no new line added to end of statement

a_list = [0,1,2,3,4,5,6,7,8,9]
print(a_list) #prints everything in brakets

for item in a_list:
    print(item, end = ",")
    
print(*a_list) #same as next line
print(a_list[0], a_list[1], a_list[2], a_list[3], a_list[4])

print(*a_list, sep =",")#puts sperator between all items