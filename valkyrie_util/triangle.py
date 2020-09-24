'''utility generators and functions related to triangle numbers'''

from typing import Generator


def triangle_num_iterator(n: int = 1) -> Generator[int, None, None]:
    '''iterates through the triangle numbers, starting at the nth one'''
    triangle_number = nth_triangle_number(n)
    while True:
        yield triangle_number
        n += 1
        triangle_number += n


def nth_triangle_number(n: int) -> int:
    '''returns the nth triangle number'''
    return n * (n + 1) // 2
