import random
primo = int(random.randint(1, 8))
secondo = int(random.randint(1, 8))
terzo = int(random.randint(1, 8))
quarto = int(random.randint(1, 8))
quinto = int(random.randint(1, 8))
array = [primo, secondo, terzo, quarto, quinto]
print(array)
print(array.count(int(input("Inserisci un numero nella lista: "))))