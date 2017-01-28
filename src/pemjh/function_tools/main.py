""" Common tools for helping with functions and performance. """


def memoize(already_known=None, key_func=None):
    """ Create a memoize function with a primed dictionary. """
    def tuple_key(*args):
        """ Wrap all of the arguments in a tuple. """
        return tuple(args)

    def decorator(function):
        """ Memoize passed function """
        known = already_known \
            if already_known is not None \
            else {}

        key_arguments = key_func \
            if key_func is not None \
            else tuple_key

        def wrapped(*args, **kwargs):
            """ Perform lookup and call function if needed """
            key = key_arguments(*args)
            if key not in known:
                known[key] = function(*args, **kwargs)
            return known[key]
        return wrapped
    return decorator
