# Collatz Conjecture - Start with a number n > 1. Find the number of steps it
# takes to reach one using the following process: If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Solution by Ender Ceylan

def collatz(num,steps):
    if num <= 1:
        return steps
    if num % 2 == 0:
        return collatz(num/2,steps+1)
    else:
        return collatz((num*3)+1,steps+1)

num = int(input("Enter a number greater than 1: "))
while num <= 1:
    num = int(input("Input must be above 1: "))
print(str(collatz(num,0)))
