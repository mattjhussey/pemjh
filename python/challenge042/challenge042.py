from __future__ import with_statement
from os.path import abspath, dirname

def scoreWord(w):
    total = 0
    for x in w:
        total += (ord(x) - 64)

    return total

def challenge042():
    with open("%s/words.txt" % dirname(abspath(__file__))) as f:
        words = []
        for line in f:
            words.extend([s.strip("\"") for s in line.split(",")])

        # Score the words
        words = sorted([scoreWord(w) for w in words])

        # Cycle through triangles
        triangle = 1
        step = 2
        nTriangleWords = 0
        while len(words) > 0:
            score = words[0]
            if score <= triangle:
                del words[0]

            if score == triangle:
                nTriangleWords += 1

            if score > triangle:
                triangle += step
                step += 1
                
    return nTriangleWords

answer = 162

if __name__ == "__main__":
    import sys
    print challenge042()
