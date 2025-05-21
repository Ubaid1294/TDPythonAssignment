# Task 1: Calculate factorial using function
#Problem Statement: Write a Python program that:
# 1.Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.Returns the calculated factorial.
# 3.Calls the function with a sample number and prints the output.

def Factorial(N):
    if N <= 1:
        return 1
    else:
        return N * Factorial(N - 1)
N = int(input("Enter a number: "))
Result = Factorial(N)
print("Factorial of",N,"is:",Result)


Result = 1
M = N

if N==0 or N==1:
    print("Factorial of",N,"is ",1)
else:
    while (N>1):
        Result *= N
        N -= 1
    print("Factorial of",M,"is:",Result)