#! /usr/bin/python3

#If you drive 10 miles, and get 20 mpg you are using half a gallon or half gas price. 
#Thus miles driven a day/mpg * gasprice = our formula
gasPrice= 2.6
mpg = 24
work = 0
yearly = 0
print(f'If gas is ${gasPrice} and you get {mpg} mpg...\n')
while work == 0:
	try:
		print(f"How many miles is it to your workplace?\nMiles: ",end='')
		work =  float(input())
		daily= work*2/mpg * gasPrice
		print(f'Everyday you spend ${(daily)} on gas\nAnd every year you spend ${(daily * 365)} on gas')
	except ValueError:
		print('Sorry, I need a number!')
		continue
while yearly == 0:
	try:
		print('\nHow many miles do you drive a year?\nMiles: ',end='')
		workB = float(input())
		yearly = workB/mpg * gasPrice
		print(f'Everyday you spend ${(yearly / 365)}\nEvery year you spend ${(yearly)} on gas\nAnd every day you drive {(workB/365)} miles.')
	except ValueError:
		print('Sorry, I need a number!')
		continue		