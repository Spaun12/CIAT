#Square Turtle

import turtle

def draw_square(turtle, size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.fillcolor("green")
t.pensize(3)
draw_square(t, 100, "red")
turtle.done()


