""" Challenge125 """


def main(limit):
    """ challenge125 """
    rt_limit = limit**0.5
    if rt_limit != int(rt_limit):
        rt_limit += 1
    rt_limit = int(rt_limit)

    found = set()
    for start in range(1, rt_limit):
        square = start**2
        for end in range(start + 1, rt_limit):
            square += end**2

            if square >= limit:
                break

            pal = str(square)
            if pal == pal[::-1]:
                found.add(square)

    return sum(found)
