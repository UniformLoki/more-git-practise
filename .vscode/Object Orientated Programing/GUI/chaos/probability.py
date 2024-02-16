#def: the probability of something occuring is
#the number of ways of achieving success out of
#the total number of possibilities that exist

#probability is a  value between 0 and 1
#0 means absolutely no chance of the event ever occuring
#1 means the event cannot be stopped from happening

#ex: probability of rolling a 2 on a six sided die
successes = 1
total_possibilities = 6

probability = successes/total_possibilities

print(probability)


#ex: probability of rolling a even number
successes = 3
total_possibilities = 6

probability = successes/total_possibilities

print(probability)


#ex: probability of heads and tails on two different coins
# the possibilities :

# first coins        second coin
# HEADS              HEADS
#HEADS               TAILS
#TAILS               HEADS
#TAILS               TAILS
successes = 1
total_possibilities = 4

probability = successes/total_possibilities

print(probability)


#0.25 for both being heads or both being tails
#.5 for both being different sides