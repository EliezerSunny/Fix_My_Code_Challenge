#!/usr/bin/python3
"""
FizzBuzz

This script prints numbers from 1 to n, with special rules for multiples
of three and five:
- For multiples of three, print "Fizz" instead of the number.
- For multiples of five, print "Buzz" instead of the number.
- For numbers which are multiples of both three and five, print "FizzBuzz".
"""

import sys

def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Missing argument")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("The provided argument is not a valid number.")
        sys.exit(1)

    fizzbuzz(number)
