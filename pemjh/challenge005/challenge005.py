def challenge005():
    primes = dict()
    max = 20

    # Loop from 2 to 20 (no need to do 1 since it has no effect
    for n in range(2, max + 1):

        # Find prime factors of the number
        for prime in range(2, max + 1):
            # How many times does the number go into n?
            count = 0
            while not (n % prime):
                count += 1
                n /= prime

            if count > 0:
                # Get the previous value
                if prime in primes:
                    previous = primes[prime]
                else:
                    previous = 0

                # If more primes are used, add them
                if count > previous:
                    primes[prime] = count

            # If n is 1 then break out
            if n == 1: break

    total = 1
    for n, p in primes.iteritems():
        total *= n**p
        
    return total

answer = 232792560

if __name__ == "__main__":
    import sys
    print challenge005()
