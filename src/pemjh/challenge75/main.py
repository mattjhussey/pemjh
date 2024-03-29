""" Challenge075 """
from pemjh.numbers import get_primitive_triples


def main():
    """ challenge075 """
    limit = 1500000
    wire_lengths = {}

    # Generate triples lower than target
    for total, length_a, length_b, length_c in \
        [(length_a + length_b + length_c,
          length_a, length_b, length_c)
         for length_a, length_b, length_c in get_primitive_triples(limit)]:

        # How many times does total go into limit?
        div = limit // total

        for k in range(1, div + 1):
            trip = k * total

            if trip in wire_lengths:
                wire_lengths[trip].add(tuple([k * length_a,
                                              k * length_b,
                                              k * length_c]))
            else:
                wire_lengths[trip] = set([tuple([k * length_a,
                                                 k * length_b,
                                                 k * length_c])])

    wire_lengths = [i[0] for i in wire_lengths.items() if len(i[1]) == 1]
    return len(wire_lengths)
