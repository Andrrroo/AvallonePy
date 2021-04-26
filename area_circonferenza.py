import math

def area_cerchio(r):
    return math.pi * r
    

def circonferenza_cerchio(r):
    return 2 * math.pi * r

raggio = input("Inserisci valore raggio: ")

print("L'area del cerchio è:", area_cerchio(raggio))

print("La circonferenza del cerchio è:", circonferenza_cerchio(raggio))