from random import randint, seed

# pseudo random appears to be random but is actually deterministic

#seed: a value used to initialize a pseudo-random process
r1 = seed(123456)
print(randint(0,100))
print(randint(0,100))
print()

r2 = Random()
r2.seed(123)
r2.randint(0,100)
print(r2)


