""" Common number functions """


def fibo():
    """ Generate an infinite fibonacci sequence. """
    current = 1
    future = 1
    while True:
        yield current
        current, future = future, current+future
