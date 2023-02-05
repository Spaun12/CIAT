#Turtle isn't this a blast

import turtle

def draw_fibonacci_spiral(t, n):
    # Set the turtle's speed
    t.speed('slow')

    # Set the starting position of the turtle
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    # Initialize variables for the fibonacci sequence
    a, b = 0, 1

    # Set the initial colors for the turtle
    colors = ['red', 'yellow', 'blue']
    t.color(colors[0])
    turtle.bgcolor('grey')

    # Draw the fibonacci spiral
    for i in range(n):
        t.forward(b)
        t.left(125)
        a, b = b, a+b

        # Change the color of the turtle
        t.color(colors[i % len(colors)])

    # Add the text "Isn't this a blast!"
    t.penup()
    t.goto(200, 0)
    t.pendown()
    t.write("Isn't this a blast!", align='center', font=('Arial', 16, 'normal'))

# Create a turtle
t = turtle.Turtle()

# Draw the fibonacci spiral
draw_fibonacci_spiral(t, 50)

# Keep the window open until it is closed
turtle.mainloop()
