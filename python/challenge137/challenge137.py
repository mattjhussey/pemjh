def fibo(n):
    a, b = 1, 2
    
    for x in xrange(n):
        yield a, b
        a, b = a + b, a + b + b

def a(n, known = {0: 0, 1: 2, 2: 15}):
    # From A081018
    if n in known:
        return known[n]

    ans = 8 * a(n - 1) - 8 * a(n - 2) + a(n - 3)
    
    known[n] = ans

    return ans

def challenge137():
    return a(15)

answer = 1120149658760

if __name__ == "__main__":
    print challenge137()
