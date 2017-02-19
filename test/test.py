def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch)

    return [root] + list(branches)

def root(t):
    return t[0]

def branches(t):
    return t[1:]

def is_tree(t):
    if type(t) != list or len(t) < 1:
        return False
    for branch in branches(t):
        if not is_tree(branch):
            return False
    return True

def is_leaf(t):
    return not branches(t)

def fib_tree(n):
    if n < 2:
        return tree(n)
    else:
        left, right = fib_tree(n - 1), fib_tree(n - 2)
        return tree(root(left) + root(right), [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum(count_leaves(b) for b in branches(t))

# partition trees

def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif n < m:
        return tree(False)
    else:
        left, right = partition_tree(n - m, m), partition_tree(n, m - 1)
        return tree(m, [left, right])


