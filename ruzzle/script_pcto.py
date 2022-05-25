import redis
from random import *
from itertools import permutations


r = redis.StrictRedis(host='10.255.237.221', port=6379, password='1357642rVi0', db=0)

r.keys()


it = "words.italian.txt"
f = open(it, 'r')
line = f.readline()




parola = input("Inserisci la parola: ")
ls = list(parola)

k = len(parola)

lista_di_liste = []
lista = []

anagrammi = []
str = ''

for i in ls:
    permutazioni = permutations(ls, k)
    lista.append(permutazioni)
    k -= 1

for z in lista:
    for o in z:
        for q in o:
            lista_di_liste.append(q)


print(lista_di_liste)



for i in lista_di_liste:
    for j in lista:
        str = str + j
    
    anagrammi.append(str)
    str = ''


anagrammi_esistenti = []

for i in anagrammi:
    if (r.sismember(it,i)):
        anagrammi_esistenti.append(i)

print("Le parole esistenti sono: ", anagrammi_esistenti)

for i in anagrammi_esistenti:
    r.sadd("parola", i)    

