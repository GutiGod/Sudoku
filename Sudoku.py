from turtle import Screen, Turtle   

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

screen.exitonclick()

