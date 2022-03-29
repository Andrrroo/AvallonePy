from guizero import *
from tkinter import *
import random
import string

#INIZIALIZZAZIONE

n = 10 
lettere = string.ascii_lowercase
stringa = ''.join((random.choice(lettere) for x in range(n)))

anagrammi = 0

def crea_lista():
    it = 'words.italian.txt'
    f = open(it, 'r')
    line = f.readline()
    valore_stringa = False

    for line in f:

        if anagrammi == line[:-1]:
            
            valore_stringa = True
    




#APPLICAZIONE
app = App(title = "Ruzz Lightyear", width=1920, height=1080)

bg = PhotoImage(file='Avallonepy/ruzzle/bg.png')
label = Label(app.tk, image=bg)
label.place(x=0, y=0)
app.full_screen = True


#INTERFACCE
locale_schermata = Window(app, title= 'Locale', width=1920, height=1080, visible= False)

label_locale = Label(locale_schermata.tk, image=bg)
label_locale.place(x=0, y=0)

locale_schermata.full_screen = True


campagna_schermata = Window(app, title='Campagna', width=1920, height=1080, visible= False)
label_campagna = Label(campagna_schermata.tk, image=bg)
label_campagna.place(x=0, y=0)

campagna_schermata.full_screen = True




#PULSANTI
def esci_function():
    app.destroy()

def locale_function():
    locale_schermata.show()

def campagna_function():
    #campagna_schermata.show()
    app.warn("Modalità in sviluppo", "Questa modalità di gioco è ancora in modalità di sviluppo. Torna presto per provarla!")

def chiudi_locale():
    locale_schermata.destroy()

def chiudi_campagna():
    campagna_schermata.destroy()




locale = PushButton(app, image='Avallonepy/ruzzle/locale.png', command=locale_function)
campagna = PushButton(app, image='Avallonepy/ruzzle/campagna.png', command=campagna_function)
esci = PushButton(app, image='Avallonepy/ruzzle/esci.png', command=esci_function)

locale_esci = PushButton(locale_schermata, command = chiudi_locale, image='Avallonepy/ruzzle/esci.png')

#campagna_esci = PushButton(campagna_schermata, command = chiudi_campagna, image='Avallonepy/ruzzle/esci.png')

gioca_locale = PushButton(locale_schermata, image='Avallonepy/ruzzle/gioca.png')




app.display()