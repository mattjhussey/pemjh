""" Challenge101 """


def get_frac(value, power, index, x_value):
    """ Work out the numerator and denomintaor for this value """
    numerator = value
    denominator = 1
    if power != 0:
        for diff in xrange(1, power + 2):
            if diff != (index + 1):
                numerator *= (x_value - diff)
                denominator *= ((index + 1) - diff)

    return numerator / denominator


def main():
    """ challenge101 """
    highest_power = 10

    # Get correct sequence
    sequence = [1 - i + i**2 - i**3 + i**4 - i**5 + i**6 - i**7 + i**8 -
                i**9 + i**10 for i in xrange(1, highest_power + 2)]

    incorrect = 0

    # Loop through powers to work out, start at 0 up to highest_power
    for power in xrange(highest_power + 1):
        # Create a sequence using the values
        # in the sequence up to power to extrapolate from

        worked_sequence = list()

        for x_value in xrange(1, highest_power + 2):
            y_value = 0
            for index, value in enumerate(sequence[:power + 1]):
                y_value += get_frac(value, power, index, x_value)

            worked_sequence.append(y_value)

        # Get first value that differs from sequence
        for correct, potential in zip(sequence, worked_sequence):
            if correct != potential:
                incorrect += potential
                break

    return incorrect
