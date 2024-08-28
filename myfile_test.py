import pytest
from myfile import is_prime
def test_is_prime_pass():
    assert is_prime(5) == True
def test_is_prime_fail():
    assert is_prime(4) == True