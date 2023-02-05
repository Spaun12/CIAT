#Turtle Changing colors

import turtle

def draw_fibonacci_spiral(t, n):
    # Set the turtle's speed
    t.speed('fastest')

    # Set the starting position of the turtle
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    # Initialize variables for the fibonacci sequence
    a, b = 0, 1

    # Set the initial colors for the turtle
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    t.color(colors[0])
    turtle.bgcolor(colors[-1])

    # Draw the fibonacci spiral
    for i in range(n):
        t.forward(b)
        t.left(90)
        a, b = b, a+b

        # Change the color of the turtle and the background
        t.color(colors[i % len(colors)])
        turtle.bgcolor(colors[(i+1) % len(colors)])

# Create a turtle
t = turtle.Turtle()

# Draw the fibonacci spiral
draw_fibonacci_spiral(t, 50)

# Keep the window open until it is closed
turtle.mainloop()
