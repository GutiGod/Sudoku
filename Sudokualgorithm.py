from random import randint, shuffle

numbers = []
for _ in range(9):
    numbers.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

print (numbers)

numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, 81):
    row = (i // 9)
    col = (i % 9)
    if numbers[row][col] == 0:
        shuffle(numberlist)
    for num in numberlist:
        if num not in numbers[row]:
            if num not in (numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col], numbers[4][col], numbers[5][col], numbers[6][col], numbers[7][col], numbers[8][col]):
                subgrid = []
                if row < 3:
                    if col < 3:
                        subgrid = [numbers[i][0:3] for i in range (0,3)]
                    elif col < 6: 
                        subgrid = [numbers[i][3:6] for i in range (0,3)]
                    else:
                        subgrid = [numbers[i][6:9] for i in range (0,3)]    
                elif row < 6:
                    if col < 3:
                        subgrid = [numbers[i][0:3] for i in range (3,6)]
                    elif col < 6: 
                        subgrid = [numbers[i][3:6] for i in range (3,6)]
                    else:
                        subgrid = [numbers[i][6:9] for i in range (3,6)]
                else:
                    if col < 3:
                        subgrid = [numbers[i][0:3] for i in range (6,9)]
                    elif col < 6: 
                        subgrid = [numbers[i][3:6] for i in range (6,9)]
                    else:
                        subgrid = [numbers[i][6:9] for i in range (6,9)]   
                if num not in (subgrid[0] + subgrid[1] + subgrid[2]):
                    numbers[row][col] = num
print (numbers)                                 
