from __future__ import with_statement
from os.path import abspath, dirname

def addRows(rows):
    while len(rows) > 1:
        r1 = rows[0]
        r2 = rows[1]

        for i in xrange(0, len(r2)):
            i1 = r1[i - 1] if i != 0 else r1[i]
            i2 = r1[i] if i != len(r2) - 1 else r1[i - 1]

            r2[i] = i1 + r2[i] if i1 < i2 else i2 + r2[i]
        
        rows = rows[1:]

    return rows[0]

def challenge081():
    side = 80
    with open("%s/matrix.txt" % dirname(abspath(__file__))) as f:
        tr = list()
        for i in xrange(2 * side - 1):
            tr.append(list())

        for n, l in enumerate(l for l in f):
            index = n
            for i in [int(i) for i in l.split(",")]:
                tr[index].append(i)
                index += 1

    # Get 0:80
    tr1 = tr[0:side]
    tr1 = addRows(tr1)
    # Get 81:
    tr2 = list(reversed(tr[side:]))
    tr2 = addRows(tr2)

    tr = addRows([tr2, tr1])

    return min(tr)

answer = 427337

if __name__ == "__main__":
    print challenge081()
