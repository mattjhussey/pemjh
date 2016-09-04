""" Challenge133 """
from pemjh.numbers import sievedPrimes


def divs_repunit(n, limit):

    return pow(10, pow(10, limit), n) == 1


def main():
    """ challenge133 """
    limit = 50
    divs = [prime for prime in list(sievedPrimes(100000))[1:]
            if not divs_repunit(prime, limit)]

    return sum(divs) + 3
