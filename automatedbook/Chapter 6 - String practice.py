orange = {'friends': 24, 'enemies': 5, 'family': 18, 'hobbies': 7}

def godamfunction(message, left, right):
    print(' Congrats bitch you did it! '.center(40,'*'))
    for k,v in message.items():
        print(k.ljust(left,'.')+(str(v).rjust(right,'.')))
print()        
print('left: ',end='')    
x = int(input())
print('right: ', end='')
y = int(input())
print()
godamfunction(orange, x, y)


https://onlinegdb.com/rJ9wVgAa4
