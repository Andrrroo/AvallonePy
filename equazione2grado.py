import math
a = int(input("Inserisci valore a: "))
b = int(input("Inserisci valore b: "))
c = int(input("Inserisci valore c: "))
print(str(a) + "x^2", "+", str(b) + "x", "+", c, "= 0")
if b != 0:  
    if c != 0:
        delta = int(math.pow(b, 2) - 4 * a * c)
        print("delta =", delta)
        if delta != 0:
            x1 = int((-1 * b + delta) / (2 * a))
            x2 = int((-1 * b - delta) / (2 * a))
            print("x1 = ", x1)
            print("x2 = ", x2)
            print("L'equazione è completa")
        else:
            x1 = (-1 * b) / (2 * a)
            x2 = x1
            print("x1 = ", x1)
            print("x2 = ", x2)
            print("L'equazione è completa")
    else:
        x1 = 0
        x2 = int(-b / a)
        print("x1 = ", x1)
        print("x2 = ", x2)
        print("L'equazione è spuria")
else:
    if c != 0:
        x1 = (math.sqrt((-c / a)))
        x2 = -(math.sqrt((-c / a)))
        print("x1 = ", x1)
        print("x2 = ", x2)
        print("L'equazione è pura")
    else:
        x1 = 0
        x2 = x1
        print("x1 = ", x1)
        print("x2 = ", x2)
        print("L'equazione è monomia")