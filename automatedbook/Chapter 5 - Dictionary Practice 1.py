allGuests = {'Alice': {'apples': 6, 'pretzels': 12},   #A list inside a list, doesn't get any more inception than that.
            'Bob': {'ham sandwiches': 3, 'apples': 2}, #Key 1 is 'Alice' with the value {stuff}
            'Carol': {'cups': 3, 'apple pies': 1}}     #{Stuff 1} has apples: 6, pretzels: 12. 

def totalBrought(guests, item): #A function that takes 2 parameters when called
    numBrought = 0      #Variable counter to be modified and returned
    for k, v in guests.items():     #Where k,v stand for key, value. Where guests is the name of the first parameter. And .items
                                    #refers to something (any variable name) within guests. 
        numBrought = numBrought + v.get(item, 0) #Counter is increased via v.get where the .get accesses a part of v and returns an integer.
                                                 #It access (item,0) where item is the 2nd parameter passed and in our first case, 'apples'.
                                                 #It searches {stuff 1} for 'apples' and that is added to numBrought counter which is returned.
    return numBrought

print('Number of things being brought:')        
print('Apples:          ' + str(totalBrought(allGuests, 'apples')))     #Simple print function with concatentation. totalBrought function is 
print('Cups:            ' + str(totalBrought(allGuests, 'cups')))       #called with the two inputs being: (allGuests, 'apples') searching 
print('Cakes:           ' + str(totalBrought(allGuests, 'cakes')))      #through the entire dictionary for 'apples' and returning the int value.
print('Ham Sandwiches:  ' + str(totalBrought(allGuests, 'ham sandwiches')))
print('Apple Pies:      ' + str(totalBrought(allGuests, 'apple pies')))
