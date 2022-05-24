# https://redis.io/commands/

import redis
from random import *

r = redis.StrictRedis(host='10.255.237.221', port=6379, password='1357642rVi0', db=0)

# inizializzo la lista delle chiavi del DB
r.keys()

# r.set('chiave, "valore')

r.set('light', 'valore')
value = r.get('light') 
print(value)

# valore incrementale

r.incr('count')
print(r.get('count'), " e incremento...")

r.incr('count')
print(r.get('count'))

print("\nControlliamo ora le chiavi: ",r.keys())

for i in range(10):
    r.rpush("lista", str(i))

print("\nestraiamo dalla lista: ")
print(r.rpush("lista", 3))

print("\noppure estraiamo la sua lunghezza ed un range: ")
print(r.llen("lista")," elementi, tra il 2 ed 8: ", r.lrange("lista", 2,8))


# https://www.html.it/pag/71229/sorted-set/

partita = "partita"

giocatori= []

#nome_utente = input("Inserisci nome utente: ")

#if nome_utente in giocatori:
#    print(nome_utente, "già esistente")
#else:
#    giocatori.append(nome_utente)
#    print("Il tuo nome utente è: ", nome_utente)

for i in range(10):
    giocatori.append("player-" + str(i))


for i in range(10):
    print(i)

    score = randint(1, 100)
    print(score)
    print(giocatori[i])

    r.zadd(partita, {giocatori[i]: score})

# PEr visualizzare in ordine ascendente tutti i giocatori:
print("\nEstrazione dalla classifica: ")

'''
ZRANGE restituisce una lista, con la classifica ordinata degli utenti
Ogni elemento della lista è una tupla con utente e punteggio
'''
classifica = r.zrange(partita, 0, -1, withscores=True)

for pl in classifica:
    print(pl)

migliore = str(classifica[len(classifica)-1][0])
peggiore = str(classifica[0][0])

print(migliore[2:10])

print("\nIl punteggio più alto è di: ",migliore[2:10] ," con ",classifica[len(classifica)-1][1], " punti" ) 
print("\nIl punteggio più basso è di: ", peggiore[2:10]," con ",classifica[0][1], " punti" ) 
