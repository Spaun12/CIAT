#My fustrated Turtle with lots adjustable. Have fun adjusting stuff labeled and not labeled.

import turtle

def draw_fibonacci_spiral(t, n):
    # Set the turtle's speed
    t.speed('slow') #(adjustable)

    # Set the starting position of the turtle
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    # Initialize variables for the fibonacci sequence
    a, b = 0, 1

    # Set the initial colors for the turtle
    colors = ['red', 'yellow', 'blue'] #(adjustable)
    t.color(colors[0])
    turtle.bgcolor('grey') #(adjustable)

    # Draw the fibonacci spiral
    for i in range(n):
        t.forward(b)
        t.left(45) #(adjustable) makes the sprial closer or more open.
        a, b = b, a+b

        # Change the color of the turtle
        t.color(colors[i % len(colors)])

    # Add the text "Isn't this a blast!"
    t.penup()
    t.goto(200, 0)
    t.pendown()
    t.color('black')
    t.write("Isn't this a blast!", align='center', font=('Arial', 32, 'normal'))

# Set the size of the turtle window to a medium size box 
turtle.screensize(600, 600) #(adjustable)

# Create a turtle
t = turtle.Turtle()

# Set the number of steps for the turtle to take. 
num_steps = 15 #(adjustable) This really helps control how long it runs.

# Draw the fibonacci spiral
draw_fibonacci_spiral(t, num_steps)

# Keep the window open until it is closed
turtle.mainloop()

