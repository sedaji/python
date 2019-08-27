# Quick little sorting algorithm made just to see if I can impliment one. Never did this before so it wasn't very intuitive. 
# Turns out, I made a Selection Sorting algorithm. Not quite as fast as merge sort, but a good accomplishment for my first time. 

import random,time
listlength = 500
unsorted = [0] * listlength
for i in range(listlength):
    unsorted[i] = random.randint(1,99)
sorted = 0

def sort(x):
    counter = 0
    for i in range(len(x)):
        for j in range(len(x)-(i+1)):
            j += 1
            if x[i] < x[i + j]:
                sorted = x[i]
            elif x[i] > x[i + j]:
                sorted = x[i + j]
                x[i + j] = x[i]
                x[i] = sorted
print(f'\n\tUnsorted list: {unsorted}\n')
start = time.time()
sort(unsorted)
end = time.time()
final = end - start
print(f'\tSorted list: {unsorted},\n\n\tElements: {listlength}\n\tTime elapsed: {final}s')
