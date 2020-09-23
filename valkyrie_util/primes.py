'''utility generators and functions related to primes'''

from typing import Dict, Generator


def is_prime(n: int) -> bool:
    '''checks if n is prime'''
    return False


def prime_factorization(n: int) -> Dict[int, int]:
    '''returns the prime factorization of n where the n equals the product of all keys ** value'''
    return {}


def prime_iterator() -> Generator[int, None, None]:
    '''iterates through all primes starting at 2'''
    yield 2
