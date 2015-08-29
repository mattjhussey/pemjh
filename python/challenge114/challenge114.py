def numVariations(blocks, tileSizes, known = dict()):
    if blocks in known:
        return known[blocks]
    nVariations = 0

    if blocks > 1:
        for tileSize in tileSizes:
            # work out with tile here
            if blocks >= tileSize:
                # Always an extra 1 block length for the spacer
                left = blocks - tileSize - 1
                if left < 0:
                    left = 0
                nVariations += numVariations(left, tileSizes)

        # work out with no tile here
        nVariations += numVariations(blocks - 1, tileSizes)

    else:
        nVariations = 1
    
    known[blocks] = nVariations

    return nVariations

def process(blocks):
    n = numVariations(blocks, range(3, blocks + 1))
    return n

def challenge114():
    blocks = 50
    return process(blocks)

answer = 16475640049

if __name__ == "__main__":
    print challenge114()
