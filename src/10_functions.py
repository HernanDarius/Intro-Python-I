# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
    if (num % 2) == 0:
        print(True)
    else:
        print(False)

is_even(3)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even_print(num):
    if (num % 2) == 0:
        print('Even!')
    else:
        print('Odd')

is_even_print(num)
