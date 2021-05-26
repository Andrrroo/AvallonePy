from array import *

def numeri_primi(Max):
    Cr = array('i', [1 for i in range(Max+1)])
    Cr[0]= 0
    Cr[1]= 0
    i = 2
    while i*i <= Max:
        if Cr[i] == 1:
            j = i+1
            while j<= Max:
                Cr[j] = 0
                j += i
            i += 1
    return Cr

def conteggio(Max, cr):
    print("Numeri Primi")
    Cont = 0
    for i in range(0, Max+1):
        if cr[i]== 1:
            print(i, end='')
            Cont += 1
    print ('\n Ci sono', conteggio(max, 0), 'numeri primi <=', max)

Max= 1000

cr = numeri_primi(Max)

conteggio(Max, cr)