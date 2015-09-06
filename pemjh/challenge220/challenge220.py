def dragonpos(n):
    c = [0,1]
    length = 1
    while length < n:
        c = [c[0]+c[1], c[1]-c[0]]
        length *= 2

    if length == n:
        return c

    m = length - n
    c2 = dragonpos(m)
    c2 = [-c2[1],c2[0]]
    return [c[0]+c2[0], c[1]+c2[1]]

def challenge220():
    return ",".join(map(str, dragonpos(10**12)))

answer = "139776,963904"

if __name__ == "__main__":
    print challenge220()
