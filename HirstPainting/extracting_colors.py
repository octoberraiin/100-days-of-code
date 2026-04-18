import colorgram

colors = colorgram.extract('image.jpg', 30)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    formatted_color = (r, g, b)
    rgb_colors.append(formatted_color)
print(rgb_colors)

# This file is not used in main.py, it is just for reference.