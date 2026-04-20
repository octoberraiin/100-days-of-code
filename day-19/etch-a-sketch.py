from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forward():
    pen.forward(20)


def move_backward():
    pen.backward(20)


def counter_clockwise():
    pen.left(10)


def clockwise():
    pen.right(10)


def clear():
    screen.resetscreen()


def hide():
    pen.penup()


def show():
    pen.pendown()


pen.speed("fastest")
pen.pensize(3)
screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")

screen.onkey(hide, "h")
screen.onkey(show, "l")

screen.exitonclick()
