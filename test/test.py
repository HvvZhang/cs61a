def tree(root, branches=[]):
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, n=0):
    print (n * " " + str(root(t)))
    for b in branches(t):
        print_tree(b, n + 2)


def square_tree(t):
    if is_leaf(t):
        return tree(root(t) ** 2)
    else:
        return tree(root(t) ** 2, [square_tree(b) for b in branches(t)])

def height_tree(t):
    if is_leaf(t):
        return 0
    else:
        return 1 + max(height_tree(b) for b in branches(t))


def tree_max(t):
    if is_leaf(t):
        return root(t)
    else:
        max_val_branches = max(tree_max(b) for b in branches(t))
        return max(root(t), max_val_branches)


def in_tree(t, x):
    if is_leaf(t):
        return root(t) == x
    else:
        return any(in_tree(b, x) for b in branches(t))


def find_path(t, x):
    """Inefficient. Going through the tree twice."""
    if not in_tree(t, x):
        return None
    elif is_leaf(t) and root(t) == x:
        return [root(t)]
    else:
        path = [find_path(b, x) for b in branches(t) if in_tree(b, x)][0]
        return [root(t)] + path

def prune(t, k):
    if k == 0:
        return tree(root(t))
    else:
        sticks = [prune(b, k - 1) for b in branches(t)]
        return tree(root(t), sticks)

def is_odd(n):
    return n % 2 != 0

def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left, right = partition_tree(n - m, m), partition_tree(n, m - 1)
        return tree(m, [left, right])

def print_partitions(t, partition=[]):
    if is_leaf(t):
        if root(t):
            print (' + '.join(partition))
    else:
        left, right = branches(t) # always has two branches
        m = str(root(t))
        print_partitions(left, partition + [m]) # The left branch has m taken out of it. So, we add it to partition
        print_partitions(right, partition) # The right branch has nothing taken out of it, yet. So we add nothing to partition



def same_tree(t1, t2):
    if is_leaf(t1) and is_leaf(t2):
        return root(t1) == root(t2)
    elif is_leaf(t1) and not is_leaf(t2):
        return False
    else:
        branches_t1 = branches(t1)
        branches_t2 = branches(t2)
        if len(branches_t1) != len(branches_t2):
            return False
        return root(t1) == root(t2) and all(same_tree(branches_t1[i], branches_t2[i]) for i in range(len(branches_t1)))











        






