""" Challenge102 """
from __future__ import with_statement


def encloses_origin(point_1, point_2, point_3):
    """ Return True if the triangle formed by the 3 points encloses the
    origin, else False. """
    # To enclose, 1 point should be left (or right) of 0
    # 0 should be between the two lines joining this point with the other 2

    # Remove invalid cases
    x12 = point_1[0] * point_2[0]
    x23 = point_2[0] * point_3[0]
    x31 = point_3[0] * point_1[0]
    if not (x12 > 0 and x23 > 0 and x31 > 0):
        # Points cross the divide
        # Find the differing point
        if x12 * x23 > 0:
            # point_2[0] is on the other side
            intercept_1 = get_y_intercept(point_2[0], point_2[1],
                                          point_1[0], point_1[1])
            intercept_2 = get_y_intercept(point_2[0], point_2[1],
                                          point_3[0], point_3[1])
        elif x23 * x31 > 0:
            # point_3[0] is on the other side
            intercept_1 = get_y_intercept(point_3[0], point_3[1],
                                          point_1[0], point_1[1])
            intercept_2 = get_y_intercept(point_3[0], point_3[1],
                                          point_2[0], point_2[1])
        else:
            # point_1[0] is on the other side
            intercept_1 = get_y_intercept(point_1[0], point_1[1],
                                          point_2[0], point_2[1])
            intercept_2 = get_y_intercept(point_1[0], point_1[1],
                                          point_3[0], point_3[1])

        if intercept_1 * intercept_2 < 0:
            return True

    return False


def get_y_intercept(x1, y1, x2, y2):
    """ Return the y intercept of the line. """
    # pylint: disable=invalid-name
    # Assume there is a run
    m = (y2 - y1) / (x2 - x1)
    # y1 = mx1 + c
    # c = y1 - mx1
    c = y1 - m * x1

    # Return y for x = 0
    return c


def main(triangles):
    """ challenge102 """
    num_enclosing = sum(1
                        for ax, ay, bx, by, cx, cy in triangles
                        if encloses_origin((ax, ay),
                                           (bx, by),
                                           (cx, cy)))

    return num_enclosing
