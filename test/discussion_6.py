# Linked List Class
class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first
    1
    >>> s.rest
    Link(2, Link(3))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __setitem__(self, index, element):
        """Sets the value at the given index to the element

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1] = 5
        >>> s
        Link(1, Link(5, Link(3)))
        >>> s[4] = 5
        Traceback (most recent call last):
        ...
        IndexError
        """
        if index == 0:
            self.first = element
        elif self.rest is Link.empty:
            raise IndexError
        else:
            self.rest[index - 1] = element

    def __contains__(self, e):
        return self.first == e or e in self.rest

    def map(self, f):
        self.first = f(self.first)
        if self.rest is not Link.empty:
            self.rest.map(f)

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

def filter_link(f, s):
    if empty(s):
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered

def extend_link(s, t):
    if empty(s):
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

# sets as unsorted sequences
def empty(s):
    return s is Link.empty


def contains(s, v):
    """
    >>> s = Link(1, Link(3, Link(2)))
    >>> contains(s, 2)
    True
    >>> contains(s, 4)
    False
    """
    if empty(s):
        return False
    else:
        return s.first == v or contains(s.rest, v)


def adjoin(s, v):
    if contains(s, v):
        return s
    else:
        return Link(v, s)

def intersect(set1, set2):
    # what a beautiful function
    in_set2 = lambda v: contains(set2, v)
    return filter_link(in_set2, set1)

def union(set1, set2):
    not_in_set2 = lambda v: not contains(set2, v)
    set1_not_set2 = filter_link(not_in_set2, set1)
    return extend_link(set1_not_set2, set2)


# sets as sorted sequences

def contains(s, v):
    """
    >>> s = Link(1, Link(2, Link(3))) # sorted list
    >>> contains(s, 2)
    True
    >>> contains(s, 5)
    False
    """
    if empty(s) or s.first > v:
        return False
    else:
        return s.first == v or contains(s.rest, v)

def adjoin(s, v):
    if empty(s) or v < s.first:
        return Link(v, s)
    elif v == s.first:
        return s
    else:
        return Link(s.first, adjoin(s.rest, v))

def intersect(set1, set2):
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect(set1.rest, set2)
        else:
            return intersect(set1, set2.rest)

def union(set1, set2):
    if empty(set2):
        return set1
    elif empty(set1):
        return set2
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, union(set1.rest, set2.rest))
        elif e1 < e2:
            return Link(e1, union(set1.rest, set2))
        else:
            return Link(e2, union(set1, set2.rest))


def add(s, v):
    assert not empty(s), "Cannot add to an empty set."
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    else:
        add(s.rest, v)  
    return v

class Tree:
    def __init__(self, root, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.root = root
        self.branches = branches

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.root, branches_str)

    def is_leaf(self):
        return not self.branches

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(Tree(1))
    1
    >>> print_tree(Tree(1, [Tree(2)]))
    1
      2
    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(t.root))
    for b in t.branches:
        print_tree(b, indent + 1)


def leaves(t):
    if t.is_leaf():
        return [t.root]
    else:
        return sum([leaves(b) for b in t.branches], [])


class BTree(Tree):
    empty = Tree(None)

    def __init__(self, root, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, root, [left, right])

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return self.left is BTree.empty and self.right is BTree.empty

    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.root)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree({0}, {1})'.format(self.root, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty'
            return 'BTree({0}, {1}, {2})'.format(self.root, self.left, self.right)

def fib_tree(n):
    """Fibonacci tree"""
    if n == 0 or n == 1:
        return BTree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = left.root + right.root
        return BTree(fib_n, left, right)

def contents(t):
    if t is BTree.empty:
        return []
    else:
        return contents(t.left) + [t.root] + contents(t.right)


# BST - each root value is larger than all entries
# in its left branch and smaller than all the entries
# in its right branch.

def bst(s):
    """Construct a binary search tree from a 
    sorted list.
    >>> bst([1, 2, 3])
    BTree(2, BTree(1), BTree(3))
    """
    if not s:
        return BTree.empty
    else:
        mid = len(s) // 2
        left, right = bst(s[:mid]), bst(s[mid + 1:])
        return BTree(s[mid], left, right)

def largest(t):
    if t.right is BTree.empty:
        return t.root
    else:
        return largest(t.right)

def second_largest(t):
    if t.is_leaf():
        return None
    elif t.right is BTree.empty:
        return largest(t.left)
    elif t.right.is_leaf():
        return t.root
    else:
        return second_largest(t.right)


# representing sets as binary search trees. 
def contains(s, v):
    if s is BTree.empty:
        return False
    elif s.root == v:
        return True
    else:
        if v > s.root:
            return contains(s.right, v)
        else:
            return contains(s.left, v)

def adjoin(s, v):
    if s is BTree.empty:
        return BTree(v)
    elif s.root == v:
        return s
    else:
        if s.root > v:
            return BTree(s.root, adjoin(s.left, v), s.right)
        else:
            return BTree(s.root, s.left, adjoin(s.right, v))


#discussion 6
def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> unique = remove_duplicates(lnk)
    >>> len(unique)
    2
    >>> len(lnk)
    2
    """    
    # cool problem!
    def helper(lnk):
        if lnk is Link.empty or lnk.rest is Link.empty:
            pass
        else:
            if lnk.rest.first == lnk.first:
                lnk.rest = lnk.rest.rest
                helper(lnk)
            else:
                helper(lnk.rest)
    helper(lnk)
    return lnk

def insert_end(lnk, v):
    if lnk.rest is Link.empty:
        lnk.rest = Link(v, lnk.rest)
    else:
        insert_end(lnk.rest, v)

def reverse(lnk):
    """
    >>> l = Link(1, Link(2, Link(3)))
    >>> reverse(l)
    Link(3, Link(2, Link(1)))
    """
    # inefficient
    def helper(lnk, prev=Link.empty):
        if lnk is Link.empty:
            return prev
        else:
            return helper(lnk.rest, Link(lnk.first, prev))
    
    new_lnk = helper(lnk)
    lnk.first = new_lnk.first
    lnk.rest = new_lnk.rest
    return new_lnk
    

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    if any(lnk is Link.empty for lnk in lst_of_lnks):
        return Link.empty
    else:
        new_link = multiply_lnks([lnk.rest for lnk in lst_of_lnks])
        from functools import reduce
        from operator import mul
        return Link(reduce(mul, [lnk.first for lnk in lst_of_lnks]), new_link)

def foo(lst):
    return [x * e for e, x in enumerate(lst) if e % 2 == 0]

def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not lst:
        return 1
    elif len(lst) == 1:
        return lst[0]
    else:
        # okay
        # so the max product either uses the first element
        # or it doesn't
        return max(max_product(lst[1:]), lst[0] * max_product(lst[2:])) 
        # And this is why recursion really is magic!

def eval_tree(t):
    """Evaluates an expression tree with functions as root
    >>> eval_tree(Tree(1))
    1
    >>> expr = Tree('*', [Tree(2), Tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(Tree('+', [expr, Tree(4), Tree(5)]))
    15
    """
    if t.is_leaf():
        return t.root
    else:
        from functools import reduce
        evaluated = [eval_tree(b) for b in t.branches]
        if t.root == '*':
            from operator import mul
            return reduce(mul, evaluated)
        elif t.root == '+':
            from operator import add
            return reduce(add, evaluated) # using reduce instead of sum to make the code look consistent


def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if not lst:
        return []
    else:
        pivot = lst[0]
        less = quicksort_list([x for x in lst[1:] if x <= pivot])
        greater = quicksort_list([x for x in lst[1:] if x > pivot])
        return less + [pivot] + greater

def quicksort_link(link):
    """
    >>> s = Link(3, Link(1, Link(4)))
    >>> quicksort_link(s)
    Link(1, Link(3, Link(4)))
    """
    if link is Link.empty:
        return link

    pivot, original_link = link.first, link
    less, greater = Link.empty, Link.empty

    while link is not Link.empty:
        curr, rest = link, link.rest
        if curr.first >= pivot:
            greater = Link(curr.first, greater) if curr is not original_link else greater
        else:
            less = Link(curr.first, less)
        link = link.rest

    less = quicksort_link(less)
    greater = quicksort_link(greater)
    new_link = extend_link(less, extend_link(Link(pivot), greater))

    return new_link

    
def widest_level(t):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ... Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = []
    level = [t]

    while level:
        levels.append([b.root for b in level])
        level = sum([b.branches for b in level], [])
    return max(levels, key=len)


# t = Tree(1, [Tree(1, [Tree(1), Tree(1)]), Tree(1)])
def redundant_map(t, f):
    t.root = f(t.root)
    new_f = lambda x: f(f(x))
    t.branches = [redundant_map(b, new_f) for b in t.branches]
    return t
























