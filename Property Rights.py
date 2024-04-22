import turtle

# Set up the initial screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("blue")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to the fastest

# Function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.begin_fill()
    pen.pendown()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

# Function to draw a triangle roof
def draw_triangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.begin_fill()
    pen.pendown()
    pen.goto(x + width / 2, y + height)
    pen.goto(x + width, y)
    pen.goto(x, y)
    pen.end_fill()

# Draw the house
draw_rectangle(-100, -50, 200, 100, "lightgrey")

# Draw the door
draw_rectangle(-20, -50, 40, 50, "brown")

# Draw the windows
for x in [-70, 30]:
    draw_rectangle(x, -20, 40, 40, "white")

# Draw the roof
draw_triangle(-120, 50, 240, 100, "black")

# Draw the chimney
draw_rectangle(60, 0, 20, 60, "lightgrey")

# Hide the turtle
pen.hideturtle()

# Keep the window open
screen.mainloop()
