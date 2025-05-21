# Task2: Using the Math Module for Calculations
# Problem Statement: Write a Python program that:
# 1. Asks the user for a number as input.
# 2. Uses the math module to calculate the:
#       - Square root of the number,
#       - Natural logarithm(log base e) of the number,
#       - Sine of the number( in radians)
# 3. Displays the calculated results.

import math

N = int(input("Enter a number: "))

if N < 1:
    print("Please enter a positive number")
else:
    print("Square root: ",math.sqrt(N))
    print("Logarithm: ",math.log(N))
    print("Sine: ",math.sin(N))