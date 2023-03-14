import turtle as t
import random

t.colormode(255)

# Parameters
no_of_circles = 40
line_width = 2
speed = "fastest"

turtle = t.Turtle()
screen = t.Screen()
turtle.width(line_width)
turtle.speed(speed)


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color


angle = 360 / no_of_circles
x = angle
for i in range(no_of_circles):
    turtle.circle(50)
    turtle.setheading(angle)
    turtle.pencolor(random_color())
    angle += x

screen.exitonclick()
