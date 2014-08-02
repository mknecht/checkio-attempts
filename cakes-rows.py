# Using a Hough transformation, from the problem space to a
# space with two parameters, as explained here:
# http://classes.soe.ucsc.edu/cmpe264/Spring08/Lec6.pdf
# https://www.cs.sfu.ca/~hamarneh/ecopy/compvis1999_hough.pdf
#
# Because evenly distributed sampling of angles did not seem to find
# the correct angles, we only try those that direct to another point.

from collections import defaultdict
from math import atan, cos, pi, sin

# Sometimes same lines are recognized as different points in parameter
# space due to marginal rounding differences.
# So, we round the float, to make sure.
precision = 4


def get_angles(p, others):
    lineangle = lambda a, b: (
        (atan(float(a[0] - b[0]) / (a[1] - b[1])))
        if (a[1] - b[1]) != 0
        else (pi / 2)
    )
    vectorangle = lambda angle: pi - ((pi / 2) - angle)
    return {vectorangle(lineangle(p, o)) for o in others}


def get_counter_array(points):
    parameterspace = defaultdict(lambda: [])
    for i, j in points:
        others = set([tuple(p) for p in points]) - {(i, j)}
        for h in get_angles((i, j), others):
            p = i * sin(h) + j * cos(h)
            # Adding points that contribute to line for better debugability.
            # A counter would have sufficed, of course.
            parameterspace[(round(p, precision), h)] += [(i, j)]
    return parameterspace


def find_minimums(counters):
    return {tuple(points) for points in counters.values() if len(points) >= 3}


def checkio(cakes):
    return len(find_minimums(get_counter_array(cakes)))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio([[4, 3], [6, 5], [9, 8], [3, 8], [9, 2]]) == 2
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
    assert checkio(
        [[2,2],[2,5],[2,8],[5,2],[5,5],[5,8],[8,2],[8,5],[8,8]]) == 8
