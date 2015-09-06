def A(n):
    rep = 1
    k = 1
    while rep % n != 0:
        k += 1
        rep = (rep * 10 + 1) % n
        
    return k

def challenge129():
    maximum = 1
    n = 1000001
    while maximum < 1000000:
        n += 2
        if (n % 5 != 0):
            an = A(n)

            if an > maximum:
                maximum = an
    return n

answer = 1000023

if __name__ == "__main__":
    import psyco
    psyco.full()
    print challenge129()
