import math

def area_cerchio(r):
    return round((math.pi * r), 2)
    

def circonferenza_cerchio(r):
    return round((2 * math.pi * r), 2)

raggio = int(input("Inserisci valore raggio: "))

print("L'area del cerchio è:", area_cerchio(raggio))

print("La circonferenza del cerchio è:", circonferenza_cerchio(raggio))