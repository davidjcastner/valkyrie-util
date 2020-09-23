import pytest
from valkyrie_util.calculate import sum_of_squares


def test_sum_of_squares() -> None:
    # normal use cases
    assert sum_of_squares(0) == 0
    assert sum_of_squares(1) == 1
    assert sum_of_squares(2) == 5
    assert sum_of_squares(3) == 14
    assert sum_of_squares(4) == 30
    assert sum_of_squares(5) == 55
    assert sum_of_squares(10) == 385

    # test invalid input
    with pytest.raises(ValueError):
        sum_of_squares(-1)
    with pytest.raises(ValueError):
        sum_of_squares(-123456789)
