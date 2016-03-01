# -*- coding: utf-8 -*-

import pytest


FIB_TABLE = [
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (11, 89)
]


LUCAS_TABLE = [
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4),
    (5, 7),
    (6, 11),
    (7, 18),
    (8, 29),
    (9, 47),
    (10, 76),
    (11, 123)
]


SUM_TABLE = [
    (2, 1, 0, 1),
    (3, 2, 0, 1),
    (4, 3, 0, 1),
    (5, 5, 0, 1),
    (6, 8, 0, 1),
    (7, 13, 0, 1),
    (8, 21, 0, 1),
    (9, 34, 0, 1),
    (10, 55, 0, 1),
    (11, 89, 0, 1),
    (1, 2, 2, 1),
    (2, 1, 2, 1),
    (3, 3, 2, 1),
    (4, 4, 2, 1),
    (5, 7, 2, 1),
    (6, 11, 2, 1),
    (7, 18, 2, 1),
    (8, 29, 2, 1),
    (9, 47, 2, 1),
    (10, 76, 2, 1),
    (11, 123, 2, 1)
]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci(n, result):
    """Assert nth number in fibonacci series."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    """Assert nth number in lucas series."""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, result, a, b', SUM_TABLE)
def test_sum_series(n, result, a, b):
    """Assert nth number in fibonacci series if no optional args."""
    from series import sum_series
    assert sum_series(n, a, b) == result



