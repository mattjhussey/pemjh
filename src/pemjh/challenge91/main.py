""" Challenge91 """


def main(grid_limit):
    """ Find the number of right angled triangles that can be made within the
    grid limit. """
    num_triangles = 0

    def points(grid_limit):
        """ Generate points up to the limit. """
        return ((x, y)
                for x in range(0, grid_limit + 1)
                for y in range(0, grid_limit + 1))

    # Loop through each point as the right angle
    for point1 in points(grid_limit):
        if point1[0] == 0 and point1[1] == 0:
            # Special case of origin
            num_triangles += grid_limit**2
        elif point1[0] == 0 or point1[1] == 0:
            # Special case
            num_triangles += grid_limit
        else:
            # Loop through other points
            for point2 in points(grid_limit):
                if point2[0] == 0 and point2[1] == 0:
                    # cannot be origin
                    pass
                if point1[0] == point2[0] and point1[1] == point2[1]:
                    # cannot be same as right angle
                    pass
                else:
                    # change:
                    if point1[1] * (point2[1] - point1[1]) == \
                       point1[0] * (point1[0] - point2[0]):
                        num_triangles += 1
    return num_triangles
