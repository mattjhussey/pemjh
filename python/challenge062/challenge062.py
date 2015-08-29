import string

def challenge062():
    cubes = dict()

    n = 1
    while True:
        potentialAnswer = n**3
        # Convert to string
        cubed = str(potentialAnswer)
        # Sort
        cubed = list(cubed)
        cubed.sort()
        cubed = string.join(cubed, "")
        # Remove leading zeros
        cubed.lstrip("0")
        # Add to dictionary
        if cubes.has_key(cubed):
            lowest, nCubes = cubes[cubed]
            lowest = lowest if lowest < potentialAnswer else potentialAnswer
            nCubes += 1
            if nCubes == 5:
                return lowest
            else:
                cubes[cubed] = [lowest, nCubes]
        else:
            cubes[cubed] = [potentialAnswer, 1]
        
        n += 1

answer = 127035954683

if __name__ == "__main__":
    print challenge062()
