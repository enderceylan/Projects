# Reverse a String - Enter a string and the program will reverse it
# and print it out.
# Solution by Ender Ceylan

def reverse(a,b):
    length = len(a)
    if length <= 0:
        return b
    else:
        b = b + a[length-1]
        a = a[:-1]
        return reverse(a,b)

x = raw_input("Enter a string: ")
print(reverse(x,''))
