import turtle as t

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["RoyalBlue", "MediumPurple", "Crimson", "DodgerBlue", "Teal", "Goldenrod", "DimGray", "ForestGreen"]

for i in range(3, 11):
    tim.color(colours[i - 3])
    for _ in range(i):
        tim.right(360 / i)
        tim.forward(100)
