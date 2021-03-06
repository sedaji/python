#! /usr/bin/python3

''' Collatz is a mathematical phenomenon. It states that given any integer, it will eventually always return the integer '1' through two forumlas. 
Even integers are divided by 2 and odd integers are multiplied by 3 and added by 1. '''

import time 

def typeit(stringX):
	for i in range(len(stringX)):
		print(stringX[i],flush=True,end="")
		time.sleep(0.03)

stringA = ("WELCOME TO COLLATZ!! Enter an integer: ")
typeit(stringA)
x = int(input())
y = str(x)
count = 0

while(x != 1):
	if (x % 2 == 0):
		print('\t' + str(x)+' / 2 = ', end ='')
		x = x // 2
	else:
		print('\t' + str(x)+ ' x 3 + 1 = ', end='')
		x = (x * 3 + 1)

	print(x,flush=True)
	time.sleep(0.005)
	count += 1
print()
time.sleep(0.7)

stringY = ("\t[" '"'+ y +'"' + " has: " + str(count) + " Iterations]")
typeit(stringY)

time.sleep(0.7)
print('\n')
