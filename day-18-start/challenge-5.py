import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########

tim.speed("fastest")
gap = 10

for _ in range(int(360 / gap)):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + gap)


screen = t.Screen()
screen.exitonclick()
