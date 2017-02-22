def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def get_middle(start, end):
    l = [start, end]
    if 1 not in l:
        return 1
    elif 2 not in l:
        return 2
    else:
        return 3

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """

    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    middle = get_middle(start, end)
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n - 1, start, middle)
        move_stack(1, start, end)
        move_stack(n - 1, middle, end)

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    p1 = lower_bound(x) - lower_bound(y)
    p2 = upper_bound(x) - upper_bound(y)
    p3 = lower_bound(x) - upper_bound(y)
    p4 = upper_bound(x) - lower_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    print (lower_bound(y), upper_bound(y))
    assert (lower_bound(y) >= 0 and upper_bound(y) >= 0) or (lower_bound(y) <= 0 and upper_bound(y) <= 0)
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(1, 2) # Replace this line!
    r2 = interval(1, 2) # Replace this line!
    return r1, r2

def multiple_references_explanation():
    return """The multiple reference problem..."""

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    fx = lambda x: a * (x ** 2) + b * (x) + c

    critical_point = - b / (2 * a)
    lower_extrema  = lower_bound(x)
    upper_extrema = upper_bound(x)

    f_at_lower, f_at_upper, f_at_cp = map(fx, lower_extrema, upper_extrema, critical_point)

    if critical_point >= lower_extrema and critical_point <= upper_extrema:
        return interval(min(f_at_upper, f_at_lower, f_at_cp), max(f_at_lower, f_at_upper, f_at_cp))
    else:
        return interval(min(f_at_upper, f_at_lower), max(f_at_upper, f_at_lower))


def compute_function(x, c):
    if len(c) == 1:
        return c[0]
    else:
        return c[0] * (x ** (len(c) - 1)) + compute_function(x, c[1:])

def compute_derivative(x, c):
    if len(c) <= 1:
        return 0
    else:
        return (len(c) - 1) * c[0] * (x ** (len(c) - 2)) + compute_derivative(x, c[1:])
    
def compute_dderivative(x, c):
    if len(c) <= 2:
        return 0
    else:
        return (len(c) - 1) * (len(c) - 2) * c[0] * (x ** (len(c) - 3)) + compute_dderivative(x, c[1:])

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def newton_update(f, df, c):
    def update(x):
        return x - (f(x, c) / df(x, c)) # should work
    return update

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def find_zero(f, df, c, guess=1):
    def near_zero(x):
        return approx_eq(f(x, c), 0)
    return improve(newton_update(f, df, c), near_zero, guess)

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    c = c[::-1] # these values were opposite to what I thought they were
    lower_extrema  = lower_bound(x)
    upper_extrema = upper_bound(x)

    # basically go through each value and test if the value is an extrema 
    size = upper_extrema - lower_extrema
    num_steps = 1000
    step_size = size / num_steps

    all_values = [lower_extrema + i * step_size for i in range(num_steps)]

    extreme_value = [find_zero(compute_derivative, compute_dderivative, c, i) for i in all_values]  # going through all the values to make sure we 
                                                                                                    # find all the extreme vals

    extreme_value = [i for i in extreme_value if i < upper_extrema and i > lower_extrema] + [lower_extrema, upper_extrema]
    f_values = [compute_function(i, c) for i in extreme_value]

    return interval(min(f_values), max(f_values))


# some quick testing for my function_value_calculators
# f = lambda x: 3 * (x ** 4) - 8 * (x ** 3) - 6 * (x ** 2) + 24 * x + 10
# df = lambda x: 12 * (x ** 3) - 24 * (x ** 2) - 12 * x + 24
# ddf = lambda x: 36 * (x ** 2) - 48 * x - 12 

# c = [10, 24, -6, -8, 3][::-1]
# print (f(2), df(2), ddf(2))
# print (compute_function(2, c), compute_derivative(2, c), compute_dderivative(2, c))
# print (find_zero(compute_derivative, compute_dderivative, c, 2)) # find zero isn't returning a zero for this value
    

    

