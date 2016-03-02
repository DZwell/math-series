

def fibonacci(n):
    """Return the nth number of the fibonacci series using recursion."""
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return the nth number of the lucas series using recursion."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """Return the nth number of either the fibonacci or the lucas series recursively."""
    if n == 0:
        return a
    elif n == 1:
        return b
    print(a, b)
    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)


def fibonacci_i(n):
    """Return the nth number of the fibonacci series using iteration."""
    x = 0
    y = 1
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    while n >= 2:
        num = x + y
        x = y
        y = num
        n -= 1
    return num


def lucas_i(n):
    """Return the nth number of the lucas series using iteration."""
    x = 2
    y = 1
    if n == 0:
        return 2
    elif n == 1:
        return 1
    while n >= 2:
        num = x + y
        x = y
        y = num
        n -= 1
    return num


def sum_series_i(n, a=0, b=1):
    """Return nth number of a mathematical series."""
    x = a
    y = b
    if n == 0:
        return a
    elif n == 1:
        return b
    while n >= 2:
        num = x + y
        x = y
        y = num
        n -= 1
    return num


if __name__ == '__main__':
    print('This module defines functions that implement mathematical series.')
    print('...\n')
    print(fibonacci.__name__ + '(n):\n')
    print('\t' + fibonacci.__doc__ + '\n')
    print(lucas.__name__ + '(n):\n')
    print('\t' + lucas.__doc__ + '\n')
    print(sum_series.__name__ + '(n):\n')
    print('\t' + sum_series.__doc__ + '\n')


