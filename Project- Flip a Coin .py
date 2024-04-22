"""
Create a Python program to simulate flipping a coin
Name: Zion Adedipe 
Purpose: Show how to use if statements in Python
"""

import random

randomint = random.randint(1, 101)

if (randomint <= 50):
    print("HEADS")
else:
    if (randomint >= 51):
        print("TAILS")
