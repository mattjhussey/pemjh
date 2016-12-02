""" Common tools for helping with functions and performance. """


def memoize(already_known=None):
    def decorator(function):
        """ Memoize passed function """
        known = already_known \
            if already_known is not None \
            else {}

        def wrapped(*args, **kwargs):
            """ Perform lookup and call function if needed """
            key = tuple(args)
            if key not in known:
                known[key] = function(*args, **kwargs)
            return known[key]
        return wrapped
    return decorator
