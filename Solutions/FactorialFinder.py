# Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence 
# n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops 
# and recursion.
# Solution by Ender Ceylan

import math

# loop solution
def factLoop(x):
    num = 1
    while (x > 0):
        num = num * x
        x = x - 1
    return num

# recursive solution    
def factRec(x,num):
    if (x == 0):
        return num
    else:
        return factRec(x-1,num*x)

x = int(input("Enter number: "))
while (x < 0):
    x = int(input("Enter number: "))
num1 = factLoop(x)
num2 = factRec(x,1)
print(str(x)+"! using loops is "+str(num1))
print(str(x)+"! using recursion is "+str(num2))
