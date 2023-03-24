""" Challenge062 """


def _encode(cube):
    print(cube,)
    stringed = str(cube)
    ordered = sorted(stringed)
    hashable = tuple(ordered)
    print(hashable)
    return hashable


def main():
    """ challenge062 """
    cubes = {}

    num = 1
    while True:
        potential_answer = num**3
        # Encode
        key = _encode(potential_answer)
        # Add to dictionary
        if key in cubes:
            lowest, num_cubes = cubes[key]
            lowest = lowest if lowest < potential_answer else potential_answer
            num_cubes += 1
            if num_cubes == 5:
                return lowest

            cubes[key] = [lowest, num_cubes]
        else:
            cubes[key] = [potential_answer, 1]

        num += 1
