'''operations for integers larger than typical data sizes'''

from typing import List


def string_to_large_number(digit_string: str) -> List[int]:
    '''converts the string of digits to a large number format'''
    return [int(c) for c in digit_string[::-1]]


def large_number_to_string(large_num: List[int]) -> str:
    '''converts the large number to a string'''
    return str().join(large_num[::-1])


def large_number_sum(large_nums: List[List[int]]) -> List[int]:
    '''sums all large numbers in the input'''
    return []


def large_number_multiply(large_num: List[int], multiplier: int) -> List[int]:
    '''returns large_num * multiplier in large number format'''
    return []
