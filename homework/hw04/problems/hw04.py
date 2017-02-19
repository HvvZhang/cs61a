HW_SOURCE_FILE = 'hw04.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3) 

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    first = 1
    second = 2
    third = 3 
    answer = 0

    if n <= 3:
        return n

    i = 3
    while i < n:
        answer = 3 * first + 2 * second + third
        first, second, third = second, third, answer
        i += 1

    return answer




def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def counter(i, value, up):
        if i == n:
            return value
        elif has_seven(i) or i % 7 == 0:
            if up:
                return counter(i + 1, value - 1, False)
            else:
                return counter(i + 1, value + 1, True)
        else:
            if up:
                return counter(i + 1, value + 1, True)
            else:
                return counter(i + 1, value - 1, False)

    return counter(1, 1, True)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def find_largest_power(k):
    if k == 0:
        return -1
    else:
        return 1 + find_largest_power(k // 2)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    power = find_largest_power(amount)
    k = pow(2, power) # largest chunk we can use.

    def helper(amount, k):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif k == 0:
            return 0
        else:
            return helper(amount - k, k) + helper(amount, k // 2)

    return helper(amount, k)


   


###################
# Extra Questions #
###################

from operator import sub, mul

fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda n: 1 if n == 1 else 

def mul(n, y):
    return n * y





