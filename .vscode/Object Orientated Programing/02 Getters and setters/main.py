from pokemon import Pokemon
from pikachu import Togedemaru
from charmander import Tepig

my_boi= Pokemon("george", 98)
print(my_boi)

p1 = Togedemaru(50)
print(p1)

p1.thunderbolt(my_boi)
print(my_boi)

p2 = Tepig("temp", 34)
print(p2)