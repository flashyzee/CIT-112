"""
Name: Zion Adedipe
Date: March 20th
Purpose: Show iteration in Python, nested loop.
"""

import turtle
yertle = turtle.Turtle()
x = -350
y = 0
flowerCount = 1
while (flowerCount <= 10):
    yertle.penup()
    yertle.goto(x, y)
    yertle.fillcolor("green")
    yertle.pendown()
   
 
    yertle.begin_fill()
    sides = 1
    while (sides <= 2):
        yertle.forward(10)  
        yertle.right(90)
        yertle.forward(20)  
        yertle.right(90)
        sides += 1
    yertle.end_fill()
   
 
    yertle.fillcolor("pink")
    yertle.begin_fill()
   
    yertle.circle(30)  
    yertle.end_fill()
   
   
    x += 60
    flowerCount += 1
    print(x, y)

