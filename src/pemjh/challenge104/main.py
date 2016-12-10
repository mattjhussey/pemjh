""" Challenge104 """


def fibo_trunc(trunc):
    a_start, b_start = 0, 1
    a_end, b_end = 0, 1

    end_trunc = 10**trunc
    start_trunc = 10**(trunc + 8)

    while 1:
        # Add,
        a_start, b_start = b_start, a_start + b_start
        a_end, b_end = b_end, a_end + b_end

        # Skim
        a_end = a_end % end_trunc
        b_end = b_end % end_trunc

        while a_start >= start_trunc:
            a_start /= 10
            b_start /= 10

        a_start_ret = a_start
        while a_start_ret > end_trunc:
            a_start_ret /= 10

        # Return
        yield a_start_ret, a_end


def main():
    """ challenge104 """
    lower_limit = 123456788  # Must be at least greater than this
    found = None
    end_point_gen = fibo_trunc(9)
    index = 0
    while not found:
        start, end = end_point_gen.next()
        index += 1
        if start > lower_limit and end > lower_limit and \
           "".join(sorted(str(start))) == "123456789" and \
           "".join(sorted(str(end))) == "123456789":
            found = index
    return found
