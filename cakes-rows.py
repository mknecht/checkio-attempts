# Using a Hough transformation, from the problem space to a
# space with two parameters, as explained her:
# two parameter
# http://classes.soe.ucsc.edu/cmpe264/Spring08/Lec6.pdf
# https://www.cs.sfu.ca/~hamarneh/ecopy/compvis1999_hough.pdf

from collections import defaultdict
from math import atan, cos, pi, sin

precision = 1
factor = 8

grad = lambda a: a * 180 / pi


def get_angles(p, others):
    lineangle = lambda a, b: (
        (atan(float(a[0] - b[0]) / (a[1] - b[1])))
        if (a[1] - b[1]) != 0
        else (pi / 2)
    )
    vectorangle = lambda angle: pi - ((pi / 2) - angle)
    return {vectorangle(lineangle(p, o)) for o in others}


def get_counter_array(points):
    parameterspace = defaultdict(lambda: [0, []])
    for i, j in points:
        others = set([tuple(p) for p in points]) - {(i, j)}
        for h in get_angles((i, j), others):
            p = i * sin(h) + j * cos(h)
            parameterspace[(round(p, factor), h)][0] += 1
            parameterspace[(round(p, factor), h)][1] += [(i, j)]
    return parameterspace


def find_minimums(counters):
    qualified = sorted([(v, k) for k, v in counters.items() if v[0] >= 3])
    print("qualified: {}".format(len(qualified)))
    for c in qualified:
        print(c)
    return qualified


def checkio(cakes):
    print("THE CAKE: {}".format(cakes))
    arr = get_counter_array(cakes)
    numlines = len(find_minimums(arr))
    print("All:")
    for k, v in sorted(arr.items()):
        print("{} -> {}".format(v, k))
    # print("nulls:")
    # print([(k[0], v) for k, v in arr.items() if k[1] == 0])
    print(numlines)
    return numlines


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio([[4, 3], [6, 5], [9, 8], [3, 8], [9, 2]]) == 2
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
    assert checkio(
        [[2,2],[2,5],[2,8],[5,2],[5,5],[5,8],[8,2],[8,5],[8,8]]) == 8
