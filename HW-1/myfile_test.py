"""
This module implements testcases.

"""
from myfile import is_prime
def test_is_prime_pass():
    """
    This module implements testcases.

    """
    assert is_prime(6) is True
def test_is_prime_fail():
    """
    This module implements testcases.

    """
    assert is_prime(7) is True
