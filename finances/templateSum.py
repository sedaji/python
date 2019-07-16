#! /usr/bin/python3

import sys
#Fill out the following 8 values. CHOOSE ONLY ONE! Annual or Monthly! 
rent = 0 
food = 0
utilites = 0 
gas = 0 
recreation = 0 
insurance = 0 
repairs = 0 #(Car maintenence)
houseHold = 0 #(ie. toilet paper, soap)

sumTotal = (rent + food + utilites + gas + recreation + insurance + repairs + houseHold)
if sumTotal == 0:
	print('\n\tAre you sure you filled out the values in the source code?\n\tPlease edit with a text editor.\n')
	sys.exit()

print(f'\n\tDid you choose monthly(m) or yearly?(y): ',end='')
metric = 'x'
while metric != 'm' and metric != 'y':
	answer = input()
	metric = answer.lower()
	if metric == 'm':
		sumTotal *=  12
	elif metric == 'y': 
		continue
	else: 
		print('\n\tType either m or y: ',end='')

hourlyPay = sumTotal / 52.143 / 40 
print(f'\n\t1. Each year on average you spend, ${sumTotal}.')
print(f'\n\t2. Each day you spend ${(sumTotal/365)}.') #look-up how to format f string to print out 2 decimal places.
print(f'\n\t3. To sustain this, if you work 40 hours a week, \n\t   you need a job that pays at least: ${hourlyPay/0.8} / hour.')
print(f'\n\t4. Each weekly paycheck should be at least ${int(hourlyPay * 40)} (after tax).\n')

