#!/usr/bin/python
# coding: utf-8

import itertools
import math

def get_quadrant(p):
    """
    Gets the quadrant for a point. Point is represented as a tuple of 2, i.e., p = (x, y)
    Returns 1 (where the signs of the two coordinates are (+,+)), 2 (−,+), 3 (−,−), and 4 (+,−).
    Note 0 is considered to have a plus sign
    """
    if p[0] >= 0 and p[1] >= 0:
        return 1
    elif p[0] < 0 and p[1] >= 0:
        return 2
    elif p[0] < 0 and p[1] < 0:
        return 3
    else:
        return 4

def is_in_all_quadrants(q):
    """
    Checks if the quadrange has a point in all 4 quadrants.
    Quadrange is represented as a tuple of 4 points, i.e., q = ((x,y), (x,y), (x,y), (x,y))
    """
    quadrants = [False, False, False, False]

    for p in q:
        quadrants[get_quadrant(p) - 1] = True

    for b in quadrants:
        if not b:
            return False

    return True

def area(q):
    """
    Area implements Green's theorem, also known as the shoelace theorem
    or the surveyors' theorem, which is the 2D case of the more general Stokes' theorem.
    Call this function only if inAllQuadrants() returns true.
    See http://code.activestate.com/recipes/578275-2d-polygon-area/
    See http://www.mathpages.com/home/kmath201/kmath201.htm
    See https://en.wikipedia.org/wiki/Shoelace_formula
    """
    ordered_points = [None] * 4

    for p in q:
        ordered_points[get_quadrant(p) - 1] = p

	# calculate the area using the Green's theorem
    total = 0
    for i, p in enumerate(ordered_points):
        v1 = p
        v2 = ordered_points[(i + 1) % 4]
        total += v1[0] * v2[1] - v1[1] * v2[0]

    return math.fabs(total / 2.0)

def is_nice(q):
    """
    is_nice returns true if the quadrangle has points in all 4 quadrants and its area is an integer
    """
    if not is_in_all_quadrants(q):
        return False

    a = area(q)

    # check if area is area is a whole number within a small epsion error
    if a - math.trunc(a) < 0.00001:
        return True

    return False

def count_nice_quadrangles(points):
    """
    count_nice_quadrangles counts the number of nice quadrangles in a given list of points
    """
    if len(points) < 4:
        return 0

    count = 0
    for q in itertools.combinations(points, 4):
        if is_nice(q):
            count += 1

    return count

def main():
    count = 0 # the total count of nice quadranges
    t = 0 # number of test cases
    n = 0 # number of points in the current test case
    i = -1 # file line index
    points = []

    while True:
        try:
            i += 1
            # Codechef want us to use raw_input instead of sys.stdin
            line = raw_input()
            if i == 0:
                # the first line indicates the numer of test cases
                t = int(line)
            elif i == 1:
                # the secod line is the number of points in the current test case
                n = int(line)
                t -= 1
            else:
                # the lines after the n are points
                words = line.split()
                x = int(words[0])
                y = int(words[1])
                p = (x, y)
                points.append(p)
                n -= 1
                if n == 0:
                    # no more points for this test case count and start a new one
                    count += count_nice_quadrangles(points)
                    i = 0
                    points = []
        except (EOFError):
            break #end of file reached

    print(count)

if __name__ == '__main__':
    main()
