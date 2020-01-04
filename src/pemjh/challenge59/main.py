""" Challenge059 """
from __future__ import with_statement
from itertools import cycle, product


def decrypt(key, code):
    """
    >> from itertools import cycle
    >>> decrypt(cycle([42]), [107])
    [65]
    """
    decryption = []
    for number in code:
        ascii_code = number ^ next(key)
        # 65 - 90 = upper case
        is_upper_case = 65 <= ascii_code <= 90
        # 97 - 123 = lower case
        is_lower_case = 97 <= ascii_code <= 123
        # 48 - 57 = numbers
        is_number = 48 <= ascii_code <= 57
        # 32 - 64 = punctuation
        is_punctuation = 32 <= ascii_code <= 64
        if is_upper_case or is_lower_case or is_number or is_punctuation:
            decryption.append(ascii_code)
        else:
            return []

    return decryption


def main(ciphers):
    """ challenge059 """
    numbers = list()
    for line in ciphers:
        numbers.extend(line.split(","))
    numbers = [int(n) for n in numbers]

    # Load ints into an array
    # Lower case 97 - 122
    # Upper case 65 - 90
    triples = product(range(97, 123), repeat=3)
    keys = [cycle(triple) for triple in triples]
    decryptions = [decrypt(key, numbers) for key in keys]
    decrypted = [sum(decryption) for decryption in decryptions if decryption]
    return decrypted[0]
