def somma_n(n):
    risultato = 0
    for num in range(int(n + 1)):
        risultato = risultato + num
    return  risultato
print(somma_n(5))
