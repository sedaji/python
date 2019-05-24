# Demonstration of fibonacci mathematical function
 

while True:
    x= 0
    y= 1
    print("fibonacci: ", end="")
    mag = int(input())
    for i in range(mag):
        print('[ '+str(i+1) +' ~ '+str(x)+' ]')
        z = x + y
        x = y
        y = z
    print()
    
