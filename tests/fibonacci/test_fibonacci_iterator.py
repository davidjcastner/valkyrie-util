from valkyrie_util.fibonacci import fibonacci_iterator


def test_fibonacci_iterator() -> None:
    # testing normal fibonacci sequence
    gen = fibonacci_iterator()
    assert next(gen) == 1
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 5
    assert next(gen) == 8
    assert next(gen) == 13
    assert next(gen) == 21
    assert next(gen) == 34
    assert next(gen) == 55
    assert next(gen) == 89

    # testing pre initialized sequence - part 1
    gen = fibonacci_iterator(a=8, b=13)
    assert next(gen) == 8
    assert next(gen) == 13
    assert next(gen) == 21
    assert next(gen) == 34
    assert next(gen) == 55
    assert next(gen) == 89

    # testing pre initialized sequence - part 2
    gen = fibonacci_iterator(a=8, b=-3)
    assert next(gen) == 8
    assert next(gen) == -3
    assert next(gen) == 5
    assert next(gen) == 2
    assert next(gen) == 7
    assert next(gen) == 9
    assert next(gen) == 16
