import turtle


def rectangle(width: int, height: int) -> None:
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)


def triangle(side: int) -> None:
    turtle.right(60)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)


def square(side: int) -> None:
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)


def hexagon(side: int) -> None:
    for _ in range(6):
        turtle.forward(side)
        turtle.right(60)


def rhombus_60_120(side: int) -> None:
    for _ in range(2):
        turtle.forward(side)
        turtle.right(60)
        turtle.forward(side)
        turtle.right(120)


def square_up(side: int) -> None:
    turtle.setheading(90)
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)


def turtle_stamp(side: int) -> None:
    turtle.forward(side)
    turtle.stamp()
    turtle.backward(side)


window = turtle.Screen()

n = int(input())
for _ in range(n):
    turtle_stamp(200)
    turtle.right(360 / n)



window.mainloop()
