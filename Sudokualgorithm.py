import random

laps = 0
subgridnum = 0
subgrid = {0: 0 , 1: 0 , 2: 0 , 3: 0 , 4: 0 , 5: 0 , 6: 0 , 7: 0 , 8: 0}
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
subgriddic = {0: 0, 1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0 , 7:0 , 8:0 , 9:0 }

def resetnums(numbers, latnums1, latnums2, latnums3, laps):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    latnums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    latnums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    latnums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    laps = 0

def numpull(numbers, laps, subgridnum):
    for _ in range (9):
        num = random.choice(numbers)
        print(num)
        numbers.remove(num)
        subgrid[laps] = num
        laps = laps + 1    
    subgriddic[subgridnum] = subgrid  
    subgridnum = subgridnum + 1
    print (subgriddic)

resetnums(0, 0, 0, 0, laps)

numpull(numbers, laps, subgridnum)
