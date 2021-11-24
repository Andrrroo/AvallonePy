word = list("giraffa")  

carattere = {}

nCaratteri = 0
count = 0

for i in word:

    if (i in carattere):  
        carattere[str(i)] += 1
    else:
        carattere[str(i)] = 1 

for i in carattere:
    if carattere[i]>1: 
        count+=1 
        nCaratteri += carattere[i] 

print(count)
print(nCaratteri)