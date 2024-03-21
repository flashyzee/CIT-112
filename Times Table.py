"""
Name: Zion Adedipe
Date: March 20th
Purpose: Show iteration in Python, times tables assignment.
"""

firstFactor = input("Please enter first factor for tables : ")

firstFactor = int(firstFactor)

secondFactor = 1
DELIMITER = 12 

while (secondFactor <= 10):
    product = firstFactor * secondFactor
    line  = str(firstFactor) + "X" + str(secondFactor) + "=" + str(product)
    print(line)
    secondFactor += 1