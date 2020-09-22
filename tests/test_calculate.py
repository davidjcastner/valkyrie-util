from valkyrie_util import Calculate


class TestCalculate:
    def test_range_sum_int(self) -> None:
        assert Calculate.range_sum_int(0, 0) == 0
        assert Calculate.range_sum_int(0, 1) == 1
        assert Calculate.range_sum_int(0, 2) == 3
        assert Calculate.range_sum_int(0, 3) == 6
        assert Calculate.range_sum_int(1, 0) == 1
        assert Calculate.range_sum_int(2, 0) == 3
        assert Calculate.range_sum_int(3, 0) == 6
        assert Calculate.range_sum_int(5, 6) == 11
        assert Calculate.range_sum_int(0, 11, 4) == 12
        assert Calculate.range_sum_int(0, 12, 4) == 24
        assert Calculate.range_sum_int(0, 13, 4) == 24
        assert Calculate.range_sum_int(3, 11, 4) == 12
        assert Calculate.range_sum_int(3, 12, 4) == 24
        assert Calculate.range_sum_int(3, 13, 4) == 24
        assert Calculate.range_sum_int(4, 11, 4) == 12
        assert Calculate.range_sum_int(4, 12, 4) == 24
        assert Calculate.range_sum_int(4, 13, 4) == 24
        assert Calculate.range_sum_int(5, 11, 4) == 8
        assert Calculate.range_sum_int(5, 12, 4) == 20
        assert Calculate.range_sum_int(5, 13, 4) == 20
