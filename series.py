import pytest


def fibonacci(n):
    """Return nth number in fibonacci series."""
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return nth number of lucas series."""
    if n == 1:
        return 2
    if n == 2:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """Return nth number in fibonaccis series unless optional args given, then lucas."""
    if a == 0 and b == 1:
        return fibonacci(n)
    if a == 2 and b == 1:
        return lucas(n)
