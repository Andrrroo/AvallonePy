import numpy as np
from guizero import *
def apri_file():
    f = open("testo.txt", 'r')
    print(f)
    f.close()


app = App(title = "Testo")
button = PushButton(app, text = "Clicca qui", command = apri_file)

app.display()
