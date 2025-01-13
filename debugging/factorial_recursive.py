#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given non-negative integer n using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input integer n.
         Returns 1 if n is 0, as 0! is defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read an integer from the command line arguments
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)
