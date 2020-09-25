'''utility functions related to the collatz sequence'''

from typing import Generator


def next_collatz(n: int) -> int:
    '''returns the next number in the collatz sequence'''
    return 0


def collatz_iterator(n: int) -> Generator[int, None, None]:
    '''iterates through the collatz sequence from n to 1'''
    yield 0


def collatz_length(n: int) -> int:
    '''returns the length of collatz sequence starting at 1'''
    return 0
