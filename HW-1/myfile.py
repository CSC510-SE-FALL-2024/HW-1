"""
This module implements the funtion to determine if a number is prime or not.

"""
def is_prime(n):
    """
    This module implements prime number check

    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
