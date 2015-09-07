from ..utilities.numbers import PrimeChecker

def challenge077():
    pc = PrimeChecker()

    nums = dict()

    num = 2
    while True:
        sums = set()

        # Is the current number a prime?
        if pc.isPrime(num):
            sums.add(tuple([num]))

        # Check for previous sums
        for a in xrange(2, num // 2 + 1):
            b = num - a

            # Collect each a sum to each b sum
            for abSums in [sorted(aSum + bSum) for aSum in nums[a] for bSum in nums[b]]:
                sums.add(tuple(abSums))

        nums[num] = sums

        if len(sums) > 5000:
            return num

        num += 1

answer = 71

if __name__ == "__main__":
    print challenge077()
