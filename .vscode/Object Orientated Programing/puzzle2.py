# use the reverse list method to create a list with two individual numbers using two for (i) loops
# the reversed loop will be turned into a integer and then added to the first number and then the 
#output will be put into a list which with check that the first and third items match

#Name: Joseph Matherne
#date: 12/5/2023
# this code finds all possible inputs for ab and cd that produce an output with the same first and last digit

def lister():
    numbers = []
    x = 0
    while x <= 9:
        y = 0
        numbers.clear()
        numbers.append(x)
        while y <= 9:
            numbers.append(y)
            y+=1
            for i in numbers:
                i = str(i)
            number = str(numbers[0])+ str(numbers[1])
            reversed_number = reverser(numbers)
            number = int(number)
            reversed_number = int(reversed_number)
            sum = number + reversed_number
            sum = str(sum)
            
            sum_numbers =[*sum]

            if len(sum_numbers) != 3:
                sum_numbers.clear()
            elif sum_numbers[0] != sum_numbers[2]:
                sum_numbers.clear()
            else:
                print (f"{number} + {reversed_number} = {sum_numbers}")
            numbers.pop(1)
        x+=1
        
def reverser(numbers:list):
    reversed_numbers = numbers.copy()
    reversed_numbers.reverse()
    for i in reversed_numbers:
        i = str(i)
    combined_reversed_numbers = str(reversed_numbers[0])+str(reversed_numbers[1])
    return (combined_reversed_numbers)
            
    

print(lister())
