#! /usr/bin/python3

# YEARLY DOLLAR TOTALS
rent = 13200 #1100 a month.
food = 3650 #$10 * 365. Where $10 = 2500(total cal) / 250(cal per dollar)
utilites = 3000 #Estimate $250 a month
gas = 1470 #13000(totalMiles) / 23(mpg) * $2.6(gasPrice)
recreation = 1000 #Estimate
insurance = 700 #Liability is cheap. 
repairs = 700 #Estimate at 4 oil changes a year + misc. 
houseHold = 500 #Estimate (ie. toilet paper, soap)
# END YEARLY TOTALS

sumTotal = (rent + food + utilites + gas + recreation + insurance + repairs + houseHold)
hourlyPay = sumTotal / 52.143 / 40 
print(f'\n\t1. Each year on average you spend, ${sumTotal}.')
print(f'\n\t2. Each day you spend ${(sumTotal/365)}.') #look-up how to format f string to print out 2 decimal places.
print(f'\n\t3. To sustain this, if you work 40 hours a week, \n\t   you need a job that pays at least: ${hourlyPay/0.8}.')
print(f'\n\t4. Each weekly paycheck should be at least ${int(hourlyPay * 40)} (after tax).\n')

#Final result = a job that pays $14.5/hr
#So the results aren't good especially with min wage being around $8 and more demanding jobs at only 12.50.
#Food is stretched pretty thin already. 
#Look into potentially biking or walking to work? 
#If I cut down on gas usage, can save $1000 a year by only driving 10 miles a day instead of 35. 