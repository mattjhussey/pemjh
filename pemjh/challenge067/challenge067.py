from __future__ import with_statement
from os.path import dirname, abspath

if __name__ == "__main__":
    import sys
    sys.path.append("..")


from ..utilities.numbers import getTriangleRouteLength

def challenge067():
    rows = []
    # Read in the file
    with open("%s/triangle.txt" % dirname(abspath(__file__))) as file:
        for line in file:
            # Create a row
            vals = [int(x) for x in line.split()]
            rows.append(vals)
    return getTriangleRouteLength(rows)

answer = 7273

if __name__ == "__main__":
    import sys
    print challenge067()
