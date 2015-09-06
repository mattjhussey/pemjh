from __future__ import with_statement
from os.path import abspath, dirname

def getNames(fp):
    names = []
    # Read in the file
    with open(fp) as f:
        next_line = f.readline()
        # Split into comma separated
        for name in next_line.split(","):
            # Strip quotes
            names.append(name.strip("\""))
    names.sort()
    return names

def scoredNames(f):
    line = 1
    origin = ord("A") - 1
    for n in getNames(f):
        score = 0
        for c in n:
            score += ord(c) - origin
        yield score * line
        line += 1
            

def challenge022():
    total = 0
    for s in scoredNames("%s/names.txt" % dirname(abspath(__file__))):
        total += s
    
    return total

answer = 871198282

if __name__ == "__main__":
    import sys
    print challenge022()
