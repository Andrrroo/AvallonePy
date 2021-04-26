import math

raggio_1 = int(input("Inserisci valore raggio: "))

def area_cerchio(raggio):
    return round((math.pi * raggio), 2)
    

def circonferenza_cerchio(raggio):
    return round((2 * math.pi * raggio), 2)

print("L'area del cerchio è:", area_cerchio(raggio_1))

print("La circonferenza del cercho è:", circonferenza_cerchio(raggio_1))