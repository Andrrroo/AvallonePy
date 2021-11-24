

str= "pop"  
it = 'words.italian.txt' 

f = open(it, 'r')
line = f.readline()

for line in f:  
    print(str) 
    if str == line[:-1]:  
        print("vero")
