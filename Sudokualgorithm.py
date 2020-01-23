from turtle import Screen, Turtle   
from random import randint, shuffle

N = 9
Size = 30
grosor = 3

def grid (turtle, N, Size, grosor):
    sign = 1
    for _ in range(2):
        for _ in range(N):
            if grosor % 3 == 0:
                turtle.pensize(3)
            else:
                turtle.pensize(1)    
            turtle.forward(Size * N)
            turtle.left(sign * 90)
            turtle.pensize(3)
            turtle.forward(Size)
            turtle.left(sign * 90)
            sign = 0 - sign
            grosor = grosor + 1

        turtle.forward(Size * N)
        [turtle.right, turtle.left][N % 2](90)
        sign = 0 - sign

screen = Screen()
yertle = Turtle()

yertle.penup()
yertle.goto(-N * Size/2, -N * Size/2) 
yertle.pendown()

grid(yertle, N, Size, grosor)

numbers = []
for _ in range(9):
    numbers.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

print (numbers)

def checkGrid(numbers):
    for row in range(0,9):
        for col in range(0,9):
            if numbers[row][col]==0:
                return False
    return True            

numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def fillGrid(numbers):
    for i in range(0,81):
        row=i//9
        col=i%9
        if numbers[row][col]==0:
            shuffle(numberlist)      
            for value in numberlist:
                if not(value in numbers[row]):
                    if not value in (numbers[0][col],numbers[1][col],numbers[2][col],numbers[3][col],numbers[4][col],numbers[5][col],numbers[6][col],numbers[7][col],numbers[8][col]):
                        square=[]
                        if row<3:
                            if col<3:
                                square=[numbers[i][0:3] for i in range(0,3)]
                            elif col<6:
                                square=[numbers[i][3:6] for i in range(0,3)]
                            else:  
                                square=[numbers[i][6:9] for i in range(0,3)]
                        elif row<6:
                            if col<3:
                                square=[numbers[i][0:3] for i in range(3,6)]
                            elif col<6:
                                square=[numbers[i][3:6] for i in range(3,6)]
                            else:  
                                square=[numbers[i][6:9] for i in range(3,6)]
                        else:
                            if col<3:
                                square=[numbers[i][0:3] for i in range(6,9)]
                            elif col<6:
                                square=[numbers[i][3:6] for i in range(6,9)]
                            else:  
                                square=[numbers[i][6:9] for i in range(6,9)]
                        if not value in (square[0] + square[1] + square[2]):
                            numbers[row][col]=value
                            if checkGrid(numbers):
                                return True
                            else:
                                if fillGrid(numbers):
                                    return True
            break
    numbers[row][col]=0             
          
fillGrid(numbers)
print (numbers)
right = 11
up = 4
cycle = 0
valuecol = 0
valuerow = 0
for _ in range(0,81):
    yertle.penup()
    yertle.goto(-N * Size/2 + right + Size * valuecol, -N * Size/2 + up + Size * valuerow)
    yertle.pendown()
    yertle.write(numbers[valuerow][valuecol], move = False, font= ("Arial", 15, "normal"))
    cycle = cycle + 1
    valuecol = valuecol + 1
    if valuecol == 9:
        valuecol = 0
        valuerow = valuerow + 1
    yertle.hideturtle()    

screen.exitonclick()
