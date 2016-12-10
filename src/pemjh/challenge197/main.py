""" Challenge197 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring


def f(x):
    return int(2**(30.403243784 - x**2)) * 10**(-9)


def main():
    """ challenge197 """
    n = 10**12
    u = -1
    i = 0

    even = 0

    found = False
    while i < n and not found:
        u = f(u)
        i += 1

        if not i & 1:
            # Even
            if u == even:
                found = True
            even = u

    return u + f(u)
