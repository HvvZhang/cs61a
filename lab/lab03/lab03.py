def remainder(x, y):
    return x % y

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a == 0:
        return b
    else:
        return gcd(remainder(b, a), a)

def is_even(n):
    return n % 2 == 0

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print (n)
    if n == 1:
        return 1
    elif is_even(n):
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)

















