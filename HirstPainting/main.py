import turtle as t
import random

t.colormode(255)
color_list = [(203, 172, 108), (153, 180, 196), (193, 161, 177), (152, 186, 174), (214, 204, 113), (207, 179, 198),
              (175, 189, 213), (160, 213, 187), (161, 203, 215), (113, 122, 185), (187, 162, 62), (215, 180, 170),
              (198, 206, 46), (105, 113, 147)]

poppy = t.Turtle()
poppy.penup()
poppy.hideturtle()

poppy.speed("fastest")
poppy.goto(-225, -220)
dot_count = 0
total_dots = 35

for dot_count in range(total_dots):
    poppy.dot(20, random.choice(color_list))
    poppy.forward(50)
    dot_count += 1

    if dot_count % 10 == 0:
        poppy.left(90)
        poppy.forward(50)
        poppy.left(90)
        poppy.forward(500)
        poppy.left(180)

screen = t.Screen()
screen.exitonclick()
