from turtle import Screen, Turtle   
import random

#number of squares and size in pixels
N = 9
Size = 30

def grid (turtle, N, Size):
    sign = 1
    for _ in range(2):
        for _ in range(N):
            turtle.forward(Size * N)
            turtle.left(sign * 90)
            turtle.forward(Size)
            turtle.left(sign * 90)
            sign = 0 - sign

        turtle.forward(Size * N)
        [turtle.right, turtle.left][N % 2](90)
        sign = 0 - sign

screen = Screen()
yertle = Turtle()

yertle.penup()
yertle.goto(-N * Size/2, -N * Size/2)  # center our grid (optional)
yertle.pendown()

grid(yertle, N, Size)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
latnums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
latnums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
latnums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last = 8
lon = 11
lar = 4
lap = 3
times = 0
column = 0
for _ in range(3):
    for _ in range(9):
        numind = random.randint(0,last)
        print (numind)
        h = numbers[numind] 
        if column == 0:
             while h not in latnums1:
                numind = random.randint(0, last)
                h = numbers[numind]
        elif column == 1:    
            while h not in latnums2:
                numind = random.randint(0, last)
                h = numbers[numind]
        elif column == 2:
            while h not in latnums3:
                numind = random.randint(0, last)
                h = numbers[numind]    

        numbers.remove(h)
        if column == 0:
            latnums1.remove(h)
        elif column == 1:
            latnums2.remove(h) 
        elif column == 2:
            latnums3.remove(h)       
        last = last - 1
        yertle.penup()
        yertle.goto(-N * Size/2 + lon, -N * Size/2 + lar)
        yertle.pendown()
        yertle.write(h, move = False, font= ("Arial", 15, "normal"))
        lap = lap - 1  
        column = column + 1 
        if lap == 0:
            lon = 11
            lar = lar + Size
            lap = 3
            column = 0
        else:
            lon = lon + Size    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]     
    last = 8  
screen.exitonclick()
