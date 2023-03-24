""" Challenge074 """
from math import factorial


def fact_sum(facts, num):
    """ Return collection of factorials for each digit in num """
    return sum(facts[c] for c in str(num))


def chain_size(num, known):
    """ Get the size of the chain starting with num """
    route = set([num])
    facts = dict((str(i), factorial(i)) for i in range(0, 10))
    step = fact_sum(facts, num)
    first_step = step
    route_length = 1
    while step not in route:
        if step in known:
            size = route_length + known[step]
            known[first_step] = size - 1
            known[num] = size
            return size

        route_length += 1
        route.add(step)
        step = fact_sum(facts, step)

    known[first_step] = route_length - 1
    known[num] = route_length
    return route_length


def main():
    """ challenge074 """
    limit = 1000000
    count = 0
    known = {}
    for i in range(1, limit + 1):
        size = chain_size(i, known)
        if size == 60:
            count += 1
    return count
