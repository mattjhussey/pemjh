""" Challenge098 """
from __future__ import with_statement


def getWord_Squares(word, square):
    word_squares = dict()
    for w, s in zip(word, square):
        if w in word_squares:
            if word_squares[w] != s:
                word_squares = None
                return
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
    mapped = list()
    for c in word:
        mapped.append(word_squares[c])

    return "".join(mapped)


def main(words):
    """ challenge098 """
    largest = 0

    groupedWords = dict()
    for line in words:
        for word in [word.strip('"') for word in line.split(',')]:
            orderedWord = "".join(sorted(word))
            if orderedWord in groupedWords:
                groupedWords[orderedWord].append(word)
            else:
                groupedWords[orderedWord] = [word]

    groupedWords = dict([(key, groupedWords[key]) for key in groupedWords
                         if len(groupedWords[key]) > 1])

    # Get squares
    squares = list()
    # 2
    squares.append([str(x*x) for x in xrange(4, 9)])
    # 3
    squares.append([str(x*x) for x in xrange(10, 31)])
    # 4
    squares.append([str(x*x) for x in xrange(32, 99)])
    # 5
    squares.append([str(x*x) for x in xrange(100, 316)])
    # 6
    squares.append([str(x*x) for x in xrange(317, 999)])
    # 7
    squares.append([str(x*x) for x in xrange(1000, 3162)])
    # 8
    squares.append([str(x*x) for x in xrange(3163, 9999)])
    # 9
    squares.append([str(x*x) for x in xrange(10000, 31622)])

    # Loop through anagrams
    for key in groupedWords:
        anagrams = groupedWords[key]
        nWords = len(anagrams)

        # Loop through word1
        for i in xrange(nWords - 1):
            word1 = anagrams[i]
            lWord = len(word1)

            # Loop through the squares for this size of word
            for potentialSquare in squares[lWord - 2]:
                # Make sure the word maps onto word1
                # (duplicate letters/numbers etc)
                # Create the map
                word_squares = getWord_Squares(word1, potentialSquare)
                if word_squares and uniqueRight(word_squares):
                    # Loop through word2
                    for j in xrange(i + 1, nWords):
                        word2 = anagrams[j]

                        word2Square = mapWord(word2, word_squares)

                        if word2Square in squares[lWord - 2]:
                            if int(word2Square) > largest:
                                largest = int(word2Square)

    return largest
