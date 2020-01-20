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
last = 8
lon = 12
lar = 5
for _ in range (9):
    numind = random.randint(0, last)
    h = (numbers[numind])
    print (h)
    yertle.penup()
    yertle.goto(-N * Size/2 + lon, -N * Size/2 + lar)
    yertle.pendown()
    yertle.write(h, move = False, font= ("Arial", 15, "normal"))
    lon = lon + 30
    numbers.remove(h)
    last = last - 1 
    if last < 1:
        continue
    
screen.exitonclick()

