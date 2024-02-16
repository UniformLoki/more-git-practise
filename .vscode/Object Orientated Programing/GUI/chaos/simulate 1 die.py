#a simulations of rolling a 6 sided die
from random import randint
values =[1,2,3,4,5,6]

counts = [0]*6 #list containing number of times each value is rolled
frequency = [0] * 6 # the frequence for rollung each value

NUM_ROLLS = 100000000

for i in range(NUM_ROLLS):
    value = randint(1,6)
    counts[value-1] += 1
    
for i in range(len(frequency)):
    frequency[i] = counts[i]/ NUM_ROLLS
    
    
print(counts)
print(frequency)