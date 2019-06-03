message = '''So Ronnie, it would appear that you have requested my phone number and alas I shall
give it to you. Here it is: 909-404-3758. Have fun with that and enjoy. Oh and here is my friend's 
phone number: 626-684-3853. My friend's phone number is 5835832869.Hahajustkiddinghereistherealnumber
hereitis:626-404-3758alrightnowgetoutofhereyouscumbag'''

def isPhoneN(text):
        
    if len(text) != 12:
        return False
    for i in range(0,3):
        if text[i].isdecimal() != True:
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if text[i].isdecimal() != True:
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if text[i].isdecimal() != True:
            return False
    return True

for i in range(len(message)):
    formated = message[i:i+12]
    if isPhoneN(formated):
        print('You found a number! ' + str(formated))
print('Done')
    
