""" Challenge077 """
from pemjh.numbers import is_prime


def main():
    """ challenge077 """
    nums = dict()

    num = 2
    while True:
        sums = set()

        # Is the current number a prime?
        if is_prime(num):
            sums.add(tuple([num]))

        # Check for previous sums
        for num_a in range(2, num // 2 + 1):
            num_b = num - num_a

            # Collect each a sum to each b sum
            for ab_sums in [sorted(aSum + bSum) for aSum in nums[num_a]
                            for bSum in nums[num_b]]:
                sums.add(tuple(ab_sums))

        nums[num] = sums

        if len(sums) > 5000:
            return num

        num += 1
