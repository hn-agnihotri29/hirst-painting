import colorgram
import turtle as turtle_modules
import random

rgb_color = []

colors = colorgram.extract("image.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)

print(rgb_color)

tim = turtle_modules.Turtle()
turtle_modules.colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()

color_list = [(182, 65, 34), (213, 149, 97), (14, 24, 42), (239, 208, 94), (241, 234, 238), (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115), (166, 141, 66), (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127), (229, 175, 161), (165, 64, 70), (167, 141, 150), (98, 113, 112), (160, 168, 165), (189, 190, 196), (217, 174, 180), (15, 25, 24), (79, 70, 43), (183, 196, 189), (119, 121, 147), (248, 196, 4)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):

    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_modules.Screen()
screen.exitonclick()
