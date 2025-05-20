# Task 1
# Problem Statement: Check if a Number is Even or Odd
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else
Number = int(input("Enter a number: "))

if Number%2 == 0:
    print(Number, "is an even number.")
else:
    print(Number, "is an odd number.")