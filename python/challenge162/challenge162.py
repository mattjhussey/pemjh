def challenge162():
    total = sum(15 * 16**(n - 1) + 41 * 14**(n - 1) - (43 * 15**(n - 1) + 13**n)for n in xrange(3, 17))
 
    return hex(total).upper()[2: -1]

answer = "3D58725572C62302"

desc = "inclusion-exclusion principle"

if __name__ == "__main__":
    print challenge162()
