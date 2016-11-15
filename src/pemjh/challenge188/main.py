""" Challenge188 """


def tetrate(a, b):
    prev = 1
    val = 1
    while b:
        val = pow(a, val, 10**8)
        if val == prev:
            b = 0
        else:
            prev = val
            b -= 1
    return val


def main():
    """ challenge188 """
    return tetrate(1777, 1855)
