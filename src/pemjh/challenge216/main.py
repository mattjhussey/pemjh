""" Challenge216 """
# pylint: disable=invalid-name


def main():
    """ challenge216 """
    nmax = 50000000

    total = 0

    p = [2 * n * n - 1 for n in range(2, nmax + 1)]
    p = [0, 0] + p

    for n in range(2, nmax + 1):
        t = p[n]
        if t == 1:
            continue
        if t == (2 * n * n - 1):
            total += 1
        k = 0
        keep_going = True
        while keep_going:
            k += 1
            i = t * k - n
            if i > nmax:
                keep_going = False
            else:
                while p[i] % t == 0:
                    p[i] //= t
        keep_going = True
        k = 0
        while keep_going:
            k += 1
            i = t * k + n
            if i > nmax:
                keep_going = False
            else:
                while p[i] % t == 0:
                    p[i] //= t
    return total
