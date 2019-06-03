import re 
string1 = 'easy peasy lemon squeezy 385-362-3738'
initialize = re.compile(r'\d{3}-\d{3}-\d{4}')
final = initialize.search(string1)
print(final.group())
