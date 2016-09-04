""" Challenge042 """
from pkgutil import get_data


def score_word(word):
    """
    >>> score_word("SKY")
    55
    """
    return sum(ord(x) - 64 for x in word)


def main():
    """ challenge042 """
    word_file = get_data(__name__, 'words.txt').split('\n')
    words = []
    for line in word_file:
        words.extend([s.strip("\"") for s in line.split(",")])

    # Score the words
    words = sorted([score_word(w) for w in words])

    # Cycle through triangles
    triangle = 1
    step = 2
    number_of_triangle_words = 0
    while len(words) > 0:
        score = words[0]
        if score <= triangle:
            del words[0]

        if score == triangle:
            number_of_triangle_words += 1

        if score > triangle:
            triangle += step
            step += 1

    return number_of_triangle_words
