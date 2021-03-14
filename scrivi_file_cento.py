from random import randint
f = open("testo.txt", "w")
testo = ""
for riga in range(0,100):
    for elemento in range(1):
        testo = testo + str(randint(1,100)) + " "

print(testo)
f.write(testo)
f.close()