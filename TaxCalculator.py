# Tax Calculator - Asks the user to enter a cost and either a country or state tax.
# It then returns the tax plus the total cost with tax.
# Solution by Ender Ceylan

import math

x = float(input("Enter cost: "))
while (x < 0):
    x = float(input("Incorrect amount. Enter cost: "))
y = float(input("Enter tax percentage: "))
while (y < 0):
    y = float(input("Incorrect amount. Enter tax percentage: "))
y = y / 100
print("Tax: $"+str(round(x*y,2)))
print("Total cost with tax: $"+str(round((x*y)+x,2)))
