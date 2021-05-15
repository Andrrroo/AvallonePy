from random import *
a = randint(0, 90)
b = randint(0, 90)
while a == b:
    b = randint(0, 90)
print(a, b)