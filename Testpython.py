# def str1():
#     print("BB")
#     print("Cricket")
#
# str1()
from math import factorial


# def add():
#     str1 = "Hello"
#     str2 = "World"
#     print(str1 + str2)
# add()

# N1 = int(input())
# N2 = int(input())
# def add(N1,N2):
#     print(N1+N2)
# add(N1,N2)


# def add(a,b):
#     c = a + b
#     return  c
# ans = add(10,20)
# print(ans)
#
# def null(a,b):
#     c = a * b
#     return c
# ans = null(2,"b ")
# print(ans)


# def add2(x,y):
#     print(x+y)
#
# add2(10,20)


# def add(x,y):
#     return x+y
#
# def square(z):
#     return z*z
# result = square(add(3,2))
# print(result)


# import math
# from math import *
# print(pi)
# print(1/pi)
# print(sqrt(4))


# import sys
# # print(sys.getrecursionlimit())
#
# sys.setrecursionlimit(20000)
#
# n=0
# def py():
#     global n
#     n = n+1
#     print("Hey Learner!",n)
#     py()
# print(py())

# Factorial
# 0! = 1
# 1! = 1 * 0! = 1 * 1 = 1
# 2! = 2 * 1! = 2 * 1 = 2
# 3! = 3 * 2! = 3 * 2 = 6
# 4! = 4 * 3! = 4 * 6 = 24
#
# n = int(input())
# def Factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * Factorial(n-1)
#
# result = Factorial(n)
# print(result)
# import mathe
#
# print(mathe.pi)


try:
    a=2
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("Other part of code is executing")