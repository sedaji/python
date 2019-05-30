orange = {'friends': 24, 'enemies': 5, 'family': 18, 'hobbies': 7}

def godamfunction(message, left, right):
    print('\n\tCongrats bitch you did it!\n')
    for k,v in message.items():
        print('\t'+k.ljust(left,'.')+(str(v).rjust(right)))
        
print('\n\tleft: ',end='')    
x = int(input())
print('\tright: ', end='')
y = int(input())
godamfunction(orange, x, y)

https://onlinegdb.com/ry11o10TE
