from utils.numbers import fibo

def challenge138():
    b1 = fibo()
    b2 = fibo()
    # Step b1 on
    for i in xrange(2):
        b1.next()
    # Step b2 on
    for i in xrange(5):
        b2.next()

    total = 0
    for i in xrange(12):
        next = b1.next() * b2.next()

        v = ((next // 2)**2 + (next + 1)**2)**0.5
        if v == int(v):
            total += int(v)
        else:
            v = ((next // 2)**2 + (next - 1)**2)**0.5
            if v == int(v):
                total += int(v)

        # Step on
        for i in xrange(2):
            b1.next(); b2.next()

    return total

answer = 1118049290473932

if __name__ == "__main__":
    print challenge138()
