from ..utilities.numbers import sievedPrimes

def primeIndices(target, indexLimit, primes, primeIndex, limit = 0, known = dict()):

    key = (target, indexLimit, primeIndex)
    if key in known:
        return known[key]

    answer = limit

    index = 3

    indexLimit = indexLimit + 1

    newProduct = index
    while newProduct <= target:
        if indexLimit != 1 and index > indexLimit:
            break

        # Recur
        mult = primes[primeIndex]**((index - 1) // 2)
        if answer != 0 and mult > answer:
#            print "over", mult, answer
            break
        else:
            next = mult * primeIndices(target // index, index - 1, primes, primeIndex + 1, answer)

            if not answer or next < answer:
                answer = next

        index += 2

        newProduct = index

    if indexLimit == 1 or index <= indexLimit:
        # Return this index
        next = primes[primeIndex]**((index - 1) // 2)
        if not answer or next < answer:
            answer = next

    known[key] = answer

    return answer

def challenge108():
    target = 1000
    primeLimit = 10000

    primes = list(sievedPrimes(primeLimit))[1:]

#    # Get suitable primeIndices
    indices = primeIndices((target * 2 - 1), 0, primes, 0)

    return indices

answer = 180180

if __name__ == "__main__":
    print challenge108()
