import random
import numpy as np

def temperatura(n):
    valori = []
    for i in range(n):
        valori.append(random.randint(10, 30))
    return valori 


print(temperatura(int(input("Inserisci numero di giorni: "))))