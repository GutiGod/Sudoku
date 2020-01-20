from turtle import Screen, Turtle

N = 9  # N by N grid
LENGTH = 30  # each grid element will be LENGTH x LENGTH pixels

def grid(turtle, n, length):
    sign = 1
    for _ in range(2):

        for _ in range(n):
            turtle.forward(length * n)
            turtle.left(sign * 90)
            turtle.forward(length)
            turtle.left(sign * 90)
            sign = 0 - sign

        turtle.forward(length * n)
        [turtle.right, turtle.left][n % 2](90)
        sign = 0 - sign

screen = Screen()
yertle = Turtle()

yertle.penup()
yertle.goto(-N * LENGTH/2, -N * LENGTH/2)  # center our grid (optional)
yertle.pendown()

grid(yertle, N, LENGTH)

screen.exitonclick()