import numpy as np
import random
primo1 = int(random.randint(1,8))
secondo1 = int(random.randint(1,8))
terzo1 = int(random.randint(1,8))
primo2 = int(random.randint(1,8))
secondo2 = int(random.randint(1,8))
terzo2 = int(random.randint(1,8))
primo3 = int(random.randint(1,8))
secondo3 = int(random.randint(1,8))
terzo3 = int(random.randint(1,8))
lista = np.array([[primo1, secondo1, terzo1],[primo2, secondo2, terzo2],[primo3, secondo3, terzo3]])

print(lista[int(input("Inserisci numero colonna da visualizzare: "))-1])