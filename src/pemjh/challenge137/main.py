""" Challenge137 """


def memoize(function):
    """ Memoize passed function """
    known = {(0,): 0, (1,): 2, (2,): 15}

    def wrapped(*args, **kwargs):
        """ Perform lookup and call function if needed """
        key = tuple(args)
        print key
        if key not in known:
            known[key] = function(*args, **kwargs)
        return known[key]
    return wrapped


@memoize
def a(n):
    # From A081018
    return 8 * a(n - 1) - 8 * a(n - 2) + a(n - 3)


def main(n):
    """ challenge137 """
    return a(n)
