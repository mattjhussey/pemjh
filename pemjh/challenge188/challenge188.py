def tetrate(a, b):
    prev = 1
    val = 1
    while b:
        val = pow(a, val, 10**8)
        if val == prev:
            return val
        prev = val
        b -= 1
    return val

def challenge188():
    return tetrate(1777, 1855)

answer = 95962097

if __name__ == "__main__":
    print challenge188()
