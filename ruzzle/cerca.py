

str= "pop"  
it = 'words.italian.txt'

f = open(it, 'r')
line = f.readline()

for line in f:  
    
    if str == line[:-1]:  
        print("vero")
    
