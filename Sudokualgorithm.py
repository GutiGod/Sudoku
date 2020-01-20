import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last = 8
for _ in range (9):
    numind = random.randint(0, last)
    h = (numbers[numind])
    print (h)   
    numbers.remove(h)
    last = last - 1 
    if last < 1:
        continue
    