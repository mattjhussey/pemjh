def f(x):
    return int(2**(30.403243784 - x**2)) * 10**(-9)

def challenge197():
    n = 10**12
    u = -1
    i = 0

    even = 0
    odd = 0

    while i < n:
        u = f(u)
        i += 1

        if not i & 1:
            # Even
            if u == even:
                break
            even = u
        
    return u + f(u)

answer = 1.710637717

if __name__ == "__main__":
    print challenge197()
