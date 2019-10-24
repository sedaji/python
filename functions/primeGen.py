''' Lists the first n prime numbers where n is any number
prime number is any number only divisible by itself and 1
ex  1 3 5 7
not primes ex. 4 6 8
'''

primes = 100
masterCount = 2     

while primes!= 0:
    count = 0
    for i in range(2,masterCount):
        if masterCount % i == 0:
            count += 1    
    if count == 0:
        print(masterCount)  
        masterCount +=1
        primes -= 1
    else: 
        masterCount += 1
