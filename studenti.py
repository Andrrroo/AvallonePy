
nome_studente1 = str(input("Inserisci nome 1° studente: "))
cognome_studente1 = str(input("Inserisci cognome 1° studente: "))
ita_studente1 = int(input("Inserisci voto italiano 1° studente: "))
mat_studente1 = int(input("Inserisci voto matematica 1° studente: "))
ing_studente1 = int(input("Inserisci voto inglese 1° studente: "))
email1 = str(input("Inserisci indirizzo email 1° studente: "))

nome_studente2 = str(input("Inserisci nome 2° studente: "))
cognome_studente2 = str(input("Inserisci cognome 2° studente: "))
ita_studente2 = int(input("Inserisci voto italiano 2° studente: "))
mat_studente2 = int(input("Inserisci voto matematica 2° studente: "))
ing_studente2 = int(input("Inserisci voto inglese 2° studente: "))
email2 = str(input("Inserisci indirizzo email 2° studente: "))

nome_studente3 = str(input("Inserisci nome 3° studente: "))
cognome_studente3 = str(input("Inserisci cognome 3° studente: "))
ita_studente3 = int(input("Inserisci voto italiano 3° studente: "))
mat_studente3 = int(input("Inserisci voto matematica 3° studente: "))
ing_studente3 = int(input("Inserisci voto inglese 3° studente: "))
email3 = str(input("Inserisci indirizzo email 3° studente: "))

nome_studente4 = str(input("Inserisci nome 4° studente: "))
cognome_studente4 = str(input("Inserisci cognome 4° studente: "))
ita_studente4 = int(input("Inserisci voto italiano 4° studente: "))
mat_studente4 = int(input("Inserisci voto matematica 4° studente: "))
ing_studente4 = int(input("Inserisci voto inglese 4° studente: "))
email4 = str(input("Inserisci indirizzo email 4° studente: "))

nome_studente5 = str(input("Inserisci nome 5° studente: "))
cognome_studente5 = str(input("Inserisci cognome 5° studente: "))
ita_studente5 = int(input("Inserisci voto italiano 5° studente: "))
mat_studente5 = int(input("Inserisci voto matematica 5° studente: "))
ing_studente5 = int(input("Inserisci voto inglese 5° studente: "))
email5 = str(input("Inserisci indirizzo email 5° studente: "))

media_studente1 = (ita_studente1 + mat_studente1 + ing_studente1) / 3
media_studente2 = (ita_studente2 + mat_studente2 + ing_studente2) / 3
media_studente3 = (ita_studente3 + mat_studente3 + ing_studente3) / 3
media_studente4 = (ita_studente4 + mat_studente4 + ing_studente4) / 3
media_studente5 = (ita_studente5 + mat_studente5 + ing_studente5) / 3

voti_studente1 = {"italiano": ita_studente1, "matematica": mat_studente1, "inglese": ing_studente1, "media": media_studente1}
voti_studente2 = {"italiano": ita_studente2, "matematica": mat_studente2, "inglese": ing_studente2, "media": media_studente2}
voti_studente3 = {"italiano": ita_studente3, "matematica": mat_studente3, "inglese": ing_studente3, "media": media_studente3}
voti_studente4 = {"italiano": ita_studente4, "matematica": mat_studente4, "inglese": ing_studente4, "media": media_studente4}
voti_studente5 = {"italiano": ita_studente5, "matematica": mat_studente5, "inglese": ing_studente5, "media": media_studente5}

studente1 = {"nome": nome_studente1, "cognome": cognome_studente1, "voti": voti_studente1}
studente2 = {"nome": nome_studente2, "cognome": cognome_studente2, "voti": voti_studente2}
studente3 = {"nome": nome_studente3, "cognome": cognome_studente3, "voti": voti_studente3}
studente4 = {"nome": nome_studente4, "cognome": cognome_studente4, "voti": voti_studente4}
studente5 = {"nome": nome_studente5, "cognome": cognome_studente5, "voti": voti_studente5}

email = input("Inserisici mail studente: ")

if email == email1:
    print(studente1)
elif email == email2:
    print(studente2)
elif email == email3:
    print(studente3)
elif email == email4:
    print(studente4)
elif email == email5:
    print(studente5)