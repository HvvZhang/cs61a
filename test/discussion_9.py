def combine(combiner, s1, s2):
    i1, i2 = iter(s1), iter(s2)
    while True:
        n1, n2 = next(i1), next(i2)
        yield combiner(n1, n2)


def generate_subsets(lst):
    if not lst:
        yield []
    else:
        new = generate_subsets(lst[1:])
        prev = generate_subsets(lst[1:])
        yield from prev
        yield from map(lambda x: [lst[0]] + x, new)




