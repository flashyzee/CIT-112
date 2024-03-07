"""
Author: Zion Adedipe
Date: 3/7/2024
Purpose: This program asks the user for two numbers, calculates their sum, differences, product, and quotient, it then displays the results.
"""
#--------------------------------

num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

add = num1 + num2
mul = num1 * num2 
sub = num1 - num2
div = int(num1 / num2)
square1 = num1 ** 2
square2 = num2 ** 2

print(f"Addition result: {add}")
print(f"Multiplication result: {mul}")
print(f"Subtraction result: {sub}")
print(f"Division result: {div}")
print(f"Squared1 result: {square1}")
print(f"Squared2 result: {square2}")
