import random

n = 0
N= int(input("Inserisci numero di punti: "))

for i in range(N):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1 :
        n += 1
pigreco = (4*n)/N

print("Pigreco è uguale a", pigreco)
