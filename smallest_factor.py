#! /usr/bin/env python3

# A script for getting the smallest prime factor of an integer.

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

print("Step 4: Initialize variable to store smallest factor")
smallest_prime_factor = None

print("Step 5: Loop through possible factors from 2 to n-1")

for i in range(2, n):
    print(f"  Check if {i} divides {n}")
    if (n % i) == 0:
        print(f"  Found a factor: {i}")
        smallest_prime_factor = i
        break

print("Step 6: Results")

if smallest_prime_factor is None:
    print(f"No factors found. {n} is prime.")
    print(n)
else:
    print(f"Smallest factor of {n} is {x}")
    print(smallest_prime_factor)
