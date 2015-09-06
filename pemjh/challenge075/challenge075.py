from utils.numbers import getPrimitiveTriples

def challenge075():
    limit = 2000000
    l = dict()

    # Generate triples lower than target
    for total, a, b, c in [(a + b + c, a, b, c) for a, b, c in getPrimitiveTriples(limit)]:
        
        # How many times does total go into limit?
        div = limit // total

        for k in xrange(1, div + 1):
            trip = k * total

            if trip in l:
                l[trip].add(tuple([k * a, k * b, k * c]))
            else:
                l[trip] = set([tuple([k * a, k * b, k * c])])

    l = [i[0] for i in l.iteritems() if len(i[1]) == 1]
    return len(l)

answer = 214954

if __name__ == "__main__":
    print challenge075()
