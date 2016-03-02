# -*- coding: utf-8 -*-

import pytest


FIB_TABLE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55)
]


LUCAS_TABLE = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11),
    (6, 18),
    (7, 29),
    (8, 47),
    (9, 76),
    (10, 123)
]


SUM_TABLE = [
    (0, 0, 0 , 1),
    (1, 1, 0, 1),
    (2, 1, 0, 1),
    (3, 2, 0, 1),
    (4, 3, 0, 1),
    (5, 5, 0, 1),
    (6, 8, 0, 1),
    (7, 13, 0, 1),
    (8, 21, 0, 1),
    (9, 34, 0, 1),
    (10, 55, 0, 1),
    (0, 2, 2, 1),
    (1, 1, 2, 1),
    (2, 3, 2, 1),
    (3, 4, 2, 1),
    (4, 7, 2, 1),
    (5, 11, 2, 1),
    (6, 18, 2, 1),
    (7, 29, 2, 1),
    (8, 47, 2, 1),
    (9, 76, 2, 1),
    (10, 123, 2, 1),
]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci(n, result):
    """Assert nth number in fibonacci series."""
    from series import fibonacci
    assert type(n) == int
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    """Assert nth number in lucas series."""
    from series import lucas
    assert type(n) == int
    assert lucas(n) == result


@pytest.mark.parametrize('n, result, a, b', SUM_TABLE)
def test_sum_series(n, result, a, b):
    """Assert nth number in fibonacci series if no optional args."""
    from series import sum_series
    assert sum_series(n, a, b) == result



