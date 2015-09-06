def numVariations(blocks, tileSizes, known = dict()):
    if blocks in known:
        return known[blocks]
    nVariations = 0

    if blocks > 1:
        for tileSize in tileSizes:
            # work out with tile here
            if blocks >= tileSize:
                nVariations += numVariations(blocks - tileSize, tileSizes)

        # work out with no tile here
        nVariations += numVariations(blocks - 1, tileSizes)

    else:
        nVariations = 1
    
    known[blocks] = nVariations

    return nVariations

def process(blocks):
    n = numVariations(blocks, [2, 3, 4])
    return n

def challenge117():
    blocks = 50
    return process(blocks)

answer = 100808458960497

if __name__ == "__main__":
    print challenge117()
