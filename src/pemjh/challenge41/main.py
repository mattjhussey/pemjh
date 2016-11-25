""" Challenge041 """
from pemjh.numbers import is_prime, permutate


def main():
    """ challenge041 """
    # loop through number of digits
    highest = 0
    for number_size in [4, 7]:
        chars = "".join([str(c) for c in xrange(1, number_size + 1)])
        for potential in [int(p)
                          for p in permutate(chars)
                          if is_prime(int(p))]:
            # if potential > highest:
            # Potential is always higher in this scenario.
            highest = potential

    return highest
