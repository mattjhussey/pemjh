""" Challenge102 """
from __future__ import with_statement


def enclosesOrigin(p1, p2, p3):
    # To enclose, 1 point should be left (or right) of 0
    # 0 should be between the two lines joining this point with the other 2

    # Remove invalid cases
    x12 = p1[0] * p2[0]
    x23 = p2[0] * p3[0]
    x31 = p3[0] * p1[0]
    if not (x12 > 0 and x23 > 0 and x31 > 0):
        # Points cross the divide
        # Find the differing point
        if x12 * x23 > 0:
            # p2[0] is on the other side
            i1 = getYIntercept(p2[0], p2[1], p1[0], p1[1])
            i2 = getYIntercept(p2[0], p2[1], p3[0], p3[1])
        elif x23 * x31 > 0:
            # p3[0] is on the other side
            i1 = getYIntercept(p3[0], p3[1], p1[0], p1[1])
            i2 = getYIntercept(p3[0], p3[1], p2[0], p2[1])
        else:
            # p1[0] is on the other side
            i1 = getYIntercept(p1[0], p1[1], p2[0], p2[1])
            i2 = getYIntercept(p1[0], p1[1], p3[0], p3[1])

        if i1 * i2 < 0:
            return True

    return False


def getYIntercept(x1, y1, x2, y2):
    # Assume there is a run
    m = (y2 - y1) / (x2 - x1)
    # y1 = mx1 + c
    # c = y1 - mx1
    c = y1 - m * x1

    # Return y for x = 0
    return c


def main(triangles):
    """ challenge102 """
    nEnclosing = sum(1
                     for ax, ay, bx, by, cx, cy in triangles
                     if enclosesOrigin((ax, ay),
                                       (bx, by),
                                       (cx, cy)))

    return nEnclosing
