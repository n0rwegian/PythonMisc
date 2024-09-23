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


window = turtle.Screen()

for _ in range(8):
    square(100)
    turtle.right(45)

window.mainloop()
