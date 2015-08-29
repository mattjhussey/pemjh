def challenge235():
    target = -600000000000
    r = 1
    dr = 0.125
    s = 0
    while abs(s - target) > 1:
        s = sum((900 - 3 * k) * r ** (k - 1) for k in range(1, 5001))
        if s > target:
            r += dr
        else:
            r -= dr
        dr /= 2
 
    return '%.12f' % r

answer = "1.002322108633"

if __name__ == "__main__":
    print challenge235()
