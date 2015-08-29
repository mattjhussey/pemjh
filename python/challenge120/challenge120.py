def highestMod(n):
    if n & 1:
        # odd
        return (n**2) - n
    else:
        return (n**2) - 2 * n

def challenge120():
    mods = [highestMod(a) for a in xrange(3, 1001)]
    return sum(mods)

answer = 333082500

if __name__ == "__main__":
    print challenge120()
