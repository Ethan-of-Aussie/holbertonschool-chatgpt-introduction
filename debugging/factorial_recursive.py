#!/usr/bin/python3
import sys

def factorial(n):
    """Function Description:
        Computes the factorial of a non-negative integer using recursion.
        Factorial of n is the product of all positive integers from n down to 1.

    Parameters:
        n (int): Non-negative integer whose factorial will be computed.

    Returns:
        int: Factorial of n, If n is 0, return 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
