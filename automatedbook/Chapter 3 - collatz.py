# Demonstration of Collatz mathematical fucntion

print('Welcome to the Collatz Circus')
while True:
    print('Enter a number: ', end='')
    
    def collatz(numA):
        if (numA % 2 == 0):
            numA = numA // 2
            return numA
        else:    
            numA = numA * 3 + 1
            return numA
    
    counter = 0
    A = int(input())
    
    while (A != 1):
        A = collatz(A)
        print(A, end=" ") 
        counter += 1
    print()
    print('Result: ' + str(counter) + ' Iterations')
    print()
