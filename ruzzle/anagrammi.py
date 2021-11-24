from itertools import permutations

lettere = list("casa")

permutazioni = list(permutations(lettere))

temp = ''
anagrammi = []


for i in permutazioni:
    for carattere in i:
        
        temp += carattere 

    
    anagrammi.append(temp)
    
    temp = ''

print(anagrammi)
