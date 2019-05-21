print("Tri Force: ",end='')
charA = '+'
charB = ' '
pHeight = int(input())
for j in range(pHeight):
    for l in range(pHeight):
        print(" ", end='')
    for i in range(pHeight-(j+1)):
        print(charB, end='')
    for h in range(j*2+1):
        print(charA, end='')
    for i in range(pHeight-(j+1)):
        print(charB, end='')    
    print()
for j in range(pHeight):
    for e in range(2):
        for i in range(pHeight-(j+1)):
            print(charB, end='')
        for h in range(j*2+1):
            print(charA, end='')
        for i in range(pHeight-(j+1)):
            print(charB, end='')
        print(end=' ')
    print()
