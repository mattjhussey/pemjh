""" Challenge5 """


def main(limit):
    """ challenge5 """
    primes = dict()
    limit = limit + 1

    # Loop from 2 to limit (no need to do 1 since it has no effect
    for number in range(2, limit):

        # Find prime factors of the number
        for prime in range(2, limit):
            # How many times does the number go into number?
            count = 0
            while not number % prime:
                count += 1
                number /= prime

            if count > 0:
                # Get the previous value
                previous = primes.get(prime, 0)

                # If more primes are used, add them
                if count > previous:
                    primes[prime] = count

    total = 1
    for number, prime in primes.items():
        total *= number**prime

    return total
