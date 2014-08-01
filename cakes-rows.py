# Using a Hough transformation, from the problem space to a
# space with two parameters, as explained her:
# two parameter
# http://classes.soe.ucsc.edu/cmpe264/Spring08/Lec6.pdf
# https://www.cs.sfu.ca/~hamarneh/ecopy/compvis1999_hough.pdf

from collections import defaultdict
from math import cos, pi, sin


def get_counter_array(points):
    dimx = reduce(max, map(lambda p: p[0], points))
    dimy = reduce(max, map(lambda p: p[1], points))
    maxlines = dimx + dimy
    parameterspace = defaultdict(lambda: [0, []])
    for i, j in points:
        for h in (float(h) / maxlines * pi for h in range(maxlines + 1)):
            p = i * sin(h) + j * cos(h)
            parameterspace[(round(p, 1), h)][0] += 1
            parameterspace[(round(p, 1), h)][1] += [(i, j)]
            if h <= .1 and len(parameterspace) < 3:
                print((round(p, 1), h))
                print(parameterspace)
    return parameterspace


def find_minimums(counters):
    print("qualified:")
    for c in [c for c in counters.values() if c[0] >= 3]:
        print(c)
    return [c for c in counters.values() if c[0] >= 3]


def checkio(cakes):
    print("THE CAKE: {}".format(cakes))
    arr = get_counter_array(cakes)
    numlines = len(find_minimums(arr))
    print("All:")
    for k, v in sorted(arr.items()):
        print("{} -> {}".format(v, k))
    print("nulls:")
    print([(k[0], v) for k, v in arr.items() if k[1] == 0])
    return numlines


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
    assert checkio(
        [[2,2],[2,5],[2,8],[5,2],[5,5],[5,8],[8,2],[8,5],[8,8]]) == 8
