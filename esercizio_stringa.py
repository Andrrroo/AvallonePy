
stringa = "modifica il codice che ti suggerisco"

print("stampo tutta la stringa", stringa)

frase = str(input("inserisci la frase: "))

i = int(0)

while i < len(frase):
    lettera = frase[i]
    print(lettera)
    i = i + 1

print(frase)
