""" Challenge098 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
from __future__ import with_statement


def getWord_Squares(word, square):
    word_squares = {}
    for w, s in zip(word, square):
        if w in word_squares:
            if word_squares[w] != s:
                word_squares = None
                return word_squares
        word_squares[w] = s

    return word_squares


def uniqueRight(word_squares):
    rights = set()
    for key in word_squares:
        if word_squares[key] in rights:
            return False

        rights.add(word_squares[key])

    return True


def mapWord(word, word_squares):
    mapped = []
    for c in word:
        mapped.append(word_squares[c])

    return "".join(mapped)


def main(words):
    """ challenge098 """
    def get_grouped_words():
        groupedWords = {}
        for line in words:
            for word in [word.strip('"') for word in line.split(',')]:
                orderedWord = "".join(sorted(word))
                if orderedWord in groupedWords:
                    groupedWords[orderedWord].append(word)
                else:
                    groupedWords[orderedWord] = [word]

        groupedWords.items()
        return {key: val for key, val in groupedWords.items()
                if len(val) > 1}
    groupedWords = get_grouped_words()

    # Get squares
    squares = []
    # 2
    squares.append([str(x*x) for x in range(4, 9)])
    # 3
    squares.append([str(x*x) for x in range(10, 31)])
    # 4
    squares.append([str(x*x) for x in range(32, 99)])
    # 5
    squares.append([str(x*x) for x in range(100, 316)])
    # 6
    squares.append([str(x*x) for x in range(317, 999)])
    # 7
    squares.append([str(x*x) for x in range(1000, 3162)])
    # 8
    squares.append([str(x*x) for x in range(3163, 9999)])
    # 9
    squares.append([str(x*x) for x in range(10000, 31622)])

    def find_largest():
        largest = 0

        # Loop through anagrams
        for key in groupedWords:
            anagrams = groupedWords[key]
            nWords = len(anagrams)

            # Loop through word1
            for i in range(nWords - 1):
                word1 = anagrams[i]
                lWord = len(word1)

                # Loop through the squares for this size of word
                for potentialSquare in squares[lWord - 2]:
                    # Make sure the word maps onto word1
                    # (duplicate letters/numbers etc)
                    # Create the map
                    word_squares = getWord_Squares(word1, potentialSquare)
                    if not (word_squares and uniqueRight(word_squares)):
                        continue

                    # Loop through word2
                    for j in range(i + 1, nWords):
                        word2 = anagrams[j]

                        word2Square = mapWord(word2, word_squares)

                        if word2Square in squares[lWord - 2] and \
                           int(word2Square) > largest:
                            largest = int(word2Square)
        return largest

    return find_largest()
