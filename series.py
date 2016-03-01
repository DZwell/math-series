import pytest


def fibonacci(n):
    """Return the nth number of the fibonacci series."""
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return the nth number of the lucas series."""
    if n == 1:
        return 2
    if n == 2:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """Return the nth number of either the fibonacci or the lucas series."""
    if a == 0 and b == 1:
        return fibonacci(n)
    if a == 2 and b == 1:
        return lucas(n)


if __name__ == '__main__':
    print('This module defines functions that implement mathematical series.')
    print('...\n')
    print(fibonacci.__name__ + '(n):\n')
    print('\t' + fibonacci.__doc__ + '\n')
    print(lucas.__name__ + '(n):\n')
    print('\t' + lucas.__doc__ + '\n')
    print(sum_series.__name__ + '(n):\n')
    print('\t' + sum_series.__doc__ + '\n')


