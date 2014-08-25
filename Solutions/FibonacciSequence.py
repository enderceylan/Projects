# Fibonacci Sequence - Enter a number and have the program generate the Fibonacci
# sequence to that number or to the Nth number.
# Solution by Ender Ceylan

x = 1
y = 1
num = int(input("Enter the amount of Fibonacci values to be viewed: "))
while num <= 0:
    num = int(input("Input must be above 0: "))
for i in range(num):
    print(str(x)+" ")
    y = (x-y)
    if i != 0:
        x = x + y
