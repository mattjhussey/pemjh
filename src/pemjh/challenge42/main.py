""" Challenge042 """


def score_word(word):
    """
    >>> score_word("SKY")
    55
    """
    return sum(ord(x) - 64 for x in word)


def main(words):
    """ challenge042 """
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
