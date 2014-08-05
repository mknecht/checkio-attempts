from math import ceil, log


def checkio(l, r):
    return sum((
        1 if (1 << i) & (l ^ r) else 0
        for i in range(int(ceil(log(l ^ r, 2))))
        )) if l != r else 0


if __name__ == '__main__':
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
    assert checkio(16, 16) == 0, "Fourth"
