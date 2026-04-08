#! /usr/bin/env python3

"A module for getting the smallest prime factor of an integer."

import sys

print("Step 1: Check for number of command-line arguments")
if len(sys.argv) != 2:
    sys.exit(sys.argv[0] + ": Expecting one command line argument -- the integer for which to get the smallest factor")

print("Step 2: Convert input argument to an integer")
n = int(sys.argv[1])
print(f"Input number received: {n}")

print("Step 3: Check if the number is positive")
if n < 1:
    sys.exit(sys.argv[0] + ": Expecting a positive integer")

print("Step 4: Initialize function to find smallest factor")

def get_smallest_prime_factor(n):
    """
    Returns the smallest integer that is a factor of `n`.
    
    If `n` is a prime number `None` is returned.

    Parameters
    ----------
    n : int
        The integer to be factored.

    Returns
    -------
    int or None
        The smallest integer that is a factor of `n`
        or None if `n` is a prime.
    """
    for i in range(2, n):
        if (n % i) == 0:
            return i
    return None

print("Step 5: Compute and print result")

result = smallest_prime_factor(n)

print("Step 6: Results")
if result is None:
    print(f"No factors found. {n} is prime.")
    print(n)
else:
    print(f"Smallest factor of {n} is {result}")
    print(result)

