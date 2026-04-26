"""Provides a simple function to count the steps it takes
to reach 1 according to the Collatz Conjecture."""

def steps(number):
    """Count the steps it takes to reach 1 according
    to the rules of the Collatz Conjecture."""
    if number < 1 or not isinstance(number, int):
        raise ValueError("Only positive integers are allowed")
    steps = 0
    result = number
    while result != 1:
        if result % 2 == 0:
            result = result / 2
        else:
            result = result * 3 + 1
        steps += 1
    return steps
