class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({0})'.format(self.first)
        else:
            return 'Link({0}, {1})'.format(self.first, repr(self.rest))



abcde = {'d':'-..', 'b':'-...', 'c':'-.-.', 'a':'.-', 'e':'.'}

def morse(code):
    root = Tree(None)
    for letter, signals in sorted(code.items()):
        tree = root
        for signal in signals:
            if signal in [b.root for b in tree.branches]:
                pass
            else:
                tree.branches.append(signal)
            tree = tree.branches[-1]
        tree.branches.append(letter)
        tree = root
    return root

def decode(signals, tree):
    """Decode signals into a letter.

    >>> t = morse(abcde)
    >>> [decode(s, t) for s in ['-..', '.', '-.-.', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:
        tree = [b for b in tree.branches if b.root == signal][0]
    leaves = [b for b in tree.branches if b.is_leaf()]
    assert len(leaves) == 1
    return leaves[0].root

















