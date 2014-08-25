# Change Return Program - The user enters a cost and then the amount of money given. 
# The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change. 
# Solution by Ender Ceylan

import math

def change(num,q,d,n,p):
    if (num <= 0):
        print(str(q)+" quarters, "+str(d)+" dimes, "+str(n)+" nickels, and "+str(p)+" pennies")
        return 1
    if (num % 25 == 0):
        return change(num-25,q+1,d,n,p)
    if (num % 10 == 0):
        return change(num-10,q,d+1,n,p)
    if (num % 5 == 0):
        return change(num-5,q,d,n+1,p)
    else:
        return change(num-1,q,d,n,p+1)

x = float(input("Enter cost: "))
y = float(input("Enter money given: "))
while (y < x):
    y = float(input("Incorrect amount. Enter money given: "))
z = round(y-x,2)
print("Change is $"+str(z))
num = int(z*100)
change(num,0,0,0,0)
