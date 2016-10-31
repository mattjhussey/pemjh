""" Challenge081 """
from __future__ import with_statement


def add_rows(rows):
    """ Reduce all rows into 1 """
    while len(rows) > 1:
        row1 = rows[0]
        row2 = rows[1]

        for i in xrange(0, len(row2)):
            index1 = row1[i - 1] if i != 0 else row1[i]
            index2 = row1[i] if i != len(row2) - 1 else row1[i - 1]

            row2[i] = index1 + row2[i] if index1 < index2 else index2 + row2[i]

        rows = rows[1:]

    return rows[0]


def main(rows):
    """ challenge081 """
    side = 80
    routes = list()
    for i in xrange(2 * side - 1):
        routes.append(list())

    for initial_index, row in enumerate(row for row in rows):
        index = initial_index
        for i in [int(j) for j in row.split(",")]:
            routes[index].append(i)
            index += 1

    # Get 0:80
    routes1 = routes[0:side]
    routes1 = add_rows(routes1)
    # Get 81:
    routes2 = list(reversed(routes[side:]))
    routes2 = add_rows(routes2)

    routes = add_rows([routes2, routes1])

    return min(routes)
