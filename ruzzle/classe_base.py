from itertools import permutations

class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)
        self.__anagrammi = anagrammi(self.__stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self):
        '''
        modificare questo metodo in modo da verificare la coerenza delle variabili di
        istanza presenti
        '''
        return 0

    def charRipetuti(self):
        '''
        questo metodo deve creare un dictionary all'interno del quale la chiave deve essere
        il singolo carattere, il valore deve essere il numero di ripetizioni di quel carattere
        
        esempi di dictionary sono presenti nel file elementi_base/dictionary.py
        '''

    def cerca(stringa):
        
        
        it = 'words.italian.txt'
        f = open(it, 'r')
        line = f.readline()

        for line in f:

            if stringa == line[: -1]:
                return true #"vero" è una stringa, deve restituire un valore booleano

        return false  # restituisce falso se non la trova
        

    def fattoriale(n):
        '''
        implementare una qualunque versione della funzione fattoriale
        questo metodo può essere omessa se si utilizza un metodo built in delle
        librerie standard
        '''

    def coeffBinom(n, k):
        ''' 
        implementare la formula del coefficiente binomiale a partire dal fattoriale
        questo metodo può essere evitato se ri richiama una delle funzioni built in
        delle librerie standard
        '''
        pass

    def anagrammi(self, stringa):
    

        self.__lettere = list(stringa)

        self.__permutazioni = list(permutations(self.__lettere))

        temp = ''
        self.__anagrammi = []


        for i in self.__permutazioni:
            for carattere in i:
        
                temp += carattere 

    
            self.__anagrammi.append(temp)
    
            temp = ''

        return self.__anagrammi # in realtà basta salvarlo nella variabile di istanza
    
        
    
    def confUtil(self):
       
       it = 'words.italian.txt'
       f = open(it, 'r')
       line = f.readline()
       


       for i in self.__anagrammi:
            stringa = self.__anagrammi[i]
            i =+ 1
            for line in f:
                if stringa == line[:-1]:
                    print(stringa)
                    return "vero"


    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        return 0

    def nPermutConRip(self):
        '''
        restituire il numero di permutazioni CON ripetizione
        '''
        return 0

    def permutSenzaRip(self):
        '''
        generare e restituire la lista di permutazioni SENZA ripetizione
        '''
        return 0

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
        '''
        restituire il numero di disposizioni semplici SENZA ripetizione
        '''
        return 0

    def nDispSemplConRip(self):
        '''
        restituire il numero di disposizioni semplici CON ripetizione
        '''
        return 0

    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        return 0


    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self):
        '''
        restituire il numero delle combinazioni SENZA ripetizione
        '''
        return 0

    def nCombSemplConRip(self):
        '''
        restituire il numero delle combinazioni CON ripetizione
        '''
        return 0

    def combSenzaRip(self):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetizione
        '''
        return 0


    def combConRip(self):
        '''
        generare e restituire la lista delle combinazioni CON ripetizione
        '''
        return 0

    # PROBABILITA'

    def probConfUtil(self):
        pass
