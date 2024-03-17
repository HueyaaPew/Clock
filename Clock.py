''' 
import turtle
import time
from math import cos, sin, radians

turtle.title("Analog Clock with Turtle Graphics")


def draw_clock_hands(length, angle, number, display_count):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(angle)

    x, y = turtle.position()
    x += cos(radians(angle)) * (radius - 20)
    y += sin(radians(angle)) * (radius - 20)
    turtle.goto(x, y)

    for i in range(display_count):
        turtle.write(f"{number} ", align="center", font=("Arial", 12, "normal"))
        x += cos(radians(angle)) * 30
        y += sin(radians(angle)) * 30
        turtle.goto(x, y)

    turtle.penup()
    turtle.goto(0, 0)


def update_clock_hands():
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    draw_clock_hands(5000, 90 - hours * 30 - minutes * 0.5, f"{hours:02d}", 4)

    draw_clock_hands(500, 90 - minutes * 6 - seconds * 0.1, f"{minutes:02d}", 5)

    draw_clock_hands(50, 90 - seconds * 6, f"{seconds:02d}", 6)


turtle.speed(99)
turtle.hideturtle()
turtle.bgcolor("white")
turtle.title("Analog Clock")

radius = 50


def update_clock():
    turtle.clear()
    update_clock_hands()
    turtle.update()
    turtle.ontimer(update_clock, 500)


update_clock()
turtle.mainloop()

'''
import turtle
import time
from math import cos, sin, radians

turtle.title("Analog Clock with Turtle Graphics")


def draw_clock_hands(length, angle, number, display_count):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(angle)

    x, y = turtle.position()
    x += cos(radians(angle)) * (radius - 20)
    y += sin(radians(angle)) * (radius - 20)
    turtle.goto(x, y)

    for i in range(display_count):
        turtle.write(f"{number} ", align="center", font=("Arial", 12, "normal"))
        x += cos(radians(angle)) * 30 
        y += sin(radians(angle)) * 30 
        turtle.goto(x, y)

    turtle.penup()
    turtle.goto(0, 0)


# Clock border?
'''
def draw_clock_border():
    turtle.penup()
    turtle.goto(-radius1, -radius1)
    turtle.pendown()
    turtle.pensize(5)
    turtle.color("black")
    turtle.goto(radius1, -radius1)
    turtle.goto(radius1, radius1)
    turtle.goto(-radius1, radius1)
    turtle.goto(-radius1, -radius1)
    turtle.penup()
'''


def update_clock_hands():
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    draw_clock_hands(50, 90 - hours * 30 - minutes * 0.5, f"{hours:02d}", 4)

    draw_clock_hands(50, 90 - minutes * 6 - seconds * 0.1, f"{minutes:02d}", 5)

    draw_clock_hands(50, 90 - seconds * 6, f"{seconds:02d}", 6)


turtle.speed(99)
turtle.hideturtle()
turtle.bgcolor("white")
turtle.title("Analog Clock")

radius = 50
radius1 = 100


def update_clock():
    turtle.clear()
    update_clock_hands()
    turtle.update()
    turtle.ontimer(update_clock, 500)


update_clock()
turtle.mainloop()
