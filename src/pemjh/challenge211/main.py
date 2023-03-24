""" Challenge211 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
from math import sqrt

sqs = [False] * 256
for initial in range(256):
    sqs[(initial * initial) & 255] = True


def addVecs(vec1, vec2):
    """
    Combine two divisor sum lists (happens when sigma2(n) is multiplied b
    sigma2(m).  All list entries that occur on only one of the lists are
    included in the returned list.
    """
    xvec = []
    for x in vec1:
        if x not in vec2:
            xvec.append(x)
    for x in vec2:
        if x not in vec1:
            xvec.append(x)
    xvec.sort()
    return xvec


def chkForMore(keyz, prodarr):
    """
    keyz is a set of identity solutions.  Prodarr is a list of products
    of 2 keyz values that form another valid number.  Generate further
    identities (if they exist) by multiplying keyz values with prodarr
    values. and if any are generated, loop again using the newly generated
    list as the next prodarr input.  Prodarr values are stored in the
    combtab list.  When no further entries can be generated, return all
    individual values in the lists in the combtab list as one list.
    """
    combtab = [prodarr]
    retval = []
    for pentry in combtab:
        keyz += pentry
    retval.sort()
    return retval


def gcd(big, lit):
    """
    Compute the greatest common denominator between two integers
    """
    while not lit == 0:
        temp = lit
        lit = big % lit
        big = temp
    return big


class primez:
    """
    Prime number generator
    """
    def __init__(self, syze):
        """
        Initialize a sieve to handle a prime number table of the size
        specified.
        """
        self.plist = []
        self.limit = syze
        self.sieve = syze * [True]
        for i in range(4, syze, 2):
            self.sieve[i] = False
        finished = False
        loop = iter(range(3, syze, 2))
        while not finished:
            nprime = next(loop)
            if self.sieve[nprime] is False:
                continue
            spt = nprime*nprime
            if spt > syze:
                finished = True
            else:
                for i in range(spt, syze, nprime):
                    self.sieve[i] = False

    def getList(self):
        """
        Return a list of prime numbers.
        """
        self.plist = [2]
        for i in range(3, self.limit, 2):
            if self.sieve[i] is True:
                self.plist.append(i)
        return self.plist

    def amIprime(self, number):
        """
        Return True if number is prime, False if it is not.
        """
        result = None
        loop = iter(self.plist)
        while result is None:
            chkn = next(loop)
            if chkn * chkn > number:
                result = True
            elif number % chkn == 0:
                result = False
        return result


class problem211:
    def __init__(self, upbound):
        """
        self.limit is the sqrt of self.biglimit.
        self.biglimit is 64,000,000 (as specified by the problem)
        """
        self.biglimit = upbound
        self.limit = int(sqrt(self.biglimit))
        self.primo = primez(self.limit)
        self.plist = self.primo.getList()
        self.getpSols()
        self.setLower()
        self.polNums()

    def doit(self):
        """
        sigma2(n * m) = sigma2(n) * sigma2(m) where n and m are relatively
        prime.

        General plan here is to:

        Calculate all solutions that have prime factors under sqrt(64m) then
        calculate all solutions that have one prime factor between sqrt(64m)
        and 64m.  Any number with two or more prime factors in that range is
        over 64m.

        solutions is a dictionary of sigma2 sums for all values x^n less
        than 8000 where x is a prime and n is a positive integer.

        Note that since entries in solutions are used to calculate if
        products involving them are square, factors of p^2 can be removed.

        Once these numbers are generated, entries of the form [x Y] and [Y z}
        are merged to form [x z] and the old entries are eliminated.

        When all merging has been done, the last entries in solutions are
        the values that we want, which should yield all solutions that
        only use factors less than sqrt(64m).  Some extra numbers can be
        gotten by multiplying identities together.

        As far as finding prime factors of solutions greater than sqrt(64m),
        a prime number x, has a divisor square some value of x^2 + 1.  This
        must match an existing (1-8000) level solution in order to be valid.
        So x^2 + 1 = Dy^2 where D is the solution for a number in the 1-8000
        range, and y is another integer.  Note that this can be simplified
        into a variation of Pell's Equation.

        So solving Pell's equation for D numbers in the range (1-8000)
        would yield those numbers with factors in the range 8000 to 64000000.

        This runs in under a second.
        """
        self.reduceSolutions()
        keyz = sorted(self.solutions.keys())
        prodarr = self.mergeIdent(keyz)
        keyz += chkForMore(keyz, prodarr)
        localans = self.solvePell()
        setx = set(keyz+localans)
        ansvec = list(setx)
        answer = 1+sum(ansvec)
        return answer

    def reduceSolutions(self):
        """
        First half of the program.

        At this point, self.solutions contains factorizations of all primes
        and their powers.  Reduce these entries by combining them iteratively,
        creating new entries (that are not prime), and removing previously
        combined entries.  When done, self.solutions should contain empty
        entries only for numbers that solve this problem.
        """
        templist = []
        while len(self.hist) > 0:
            minval = self.limit
            for j, val in self.hist.items():
                if val == minval:
                    lvec = self.getSame(j, val)
                    ok = True
                    for k in lvec:
                        if k in templist:
                            ok = False
                            break
                    if ok:
                        templist += lvec
                if val < minval:
                    minval = val
                    templist = [] + self.getSame(j, val)
            for j in range(0, len(templist), minval):
                mergev = templist[j:j+minval]
                self.reducev(mergev)
            self.polNums()

    def mergeIdent(self, keyz):
        """
        The previous routine does not account for identities that can be
        multiplied together.  This routine finds those identity products
        consisting of two identity values and adds them to the solution list.
        ChkForMore uses this data as a starting point to determine if there are
        identity value combinations of 3 or more that can be multiplied
        together.
        """
        prodarr = []
        stind = 1
        tval = keyz[0] * keyz[stind]
        while tval < self.biglimit:
            stind += 1
            tval = keyz[0] * keyz[stind]
        for i1 in range(0, stind-1):
            for i2 in range(i1+1, stind):
                if gcd(keyz[i2], keyz[i1]) != 1:
                    continue
                prod = keyz[i1]*keyz[i2]
                if prod > self.biglimit:
                    continue
                prodarr.append(prod)
        prodarr.sort()
        return prodarr

    def solvePell(self):
        """
        Second half of the program.

        Find all unfactorable numbers greater than 8000 that can be multiplied
        by numbers below 8000 that form a valid solution.
        Essentially, this code loops for all possible factors under 8000,
        solves the Pell's equation x^2 - D * y^2 = -1, and multiplies any
        valid number produced with entries under 8000 that reduce to D.
        This works because the only numbers greater tha 8000 that qualify are
        prime, the sigma2 value for a prime number n is n^2 + 1, and because
        sigma2 values can be multiplied together.

        The Pell equation algorithm here is based off Lagrange-Matthews-Mollin
        algorithm.
        """
        localans = []

        def acc():
            axval = [1, 0]
            bxval = [0, 1]
            pval = 0
            qval = 1
            sqrtd = sqrt(i)
            anum = int((pval+sqrtd)/qval)
            aval = anum*axval[0] + axval[1]
            bval = anum*bxval[0] + bxval[1]
            origa = anum
            period = 0
            loop2 = iter(range(self.limit))
            finished = False
            while not finished:
                c = next(loop2)
                if period == 0 and anum == origa*2:
                    period = c
                    if period % 2 == 0:
                        break
                    localans.extend(self.chkPellVal(axval[0], self.lowhist[i]))
                if period > 0:
                    temp = c + 1
                    if temp % period == 0 and \
                       temp / period % 2 == 1:
                        localans.extend(self.chkPellVal(aval,
                                                        self.lowhist[i]))
                bxval[1] = bxval[0]
                bxval[0] = bval
                axval[1] = axval[0]
                axval[0] = aval
                pval = anum*qval - pval
                qval = (i-pval*pval)/qval
                anum = int((pval+sqrtd)/qval)
                aval = anum*axval[0] + axval[1]
                bval = anum*bxval[0] + bxval[1]
                if axval[0] > self.biglimit:
                    finished = True

        keyl = sorted(self.lowhist.keys())
        loop1 = iter(keyl[1:])
        finished1 = False
        while not finished1:
            i = next(loop1)
            if i > self.biglimit/2:
                finished1 = True
            else:
                acc()
        return localans

    def chkPellVal(self, aval, histind):
        """
        aval is an x value in a solved Pell equation.
        histind is the set of numbers which can be multiplied by aval to
        reduce down to a set of solutions.
        if aval is greater than 8000, and if aval is prime, then it's a
        candidate for possible solutions where one factor is greater than
        8000.  The code then multiplies that number by histind values to
        generate valid solutions.
        """
        retval = []
        if aval < self.limit:
            return []
        if self.primo.amIprime(aval):
            for i in histind:
                nnum = aval * i
                if nnum > self.biglimit:
                    break
                retval.append(nnum)
        return retval

    def findSol(self, value):
        """
        Input parameter: value
        Returns: Divisor sum square for value as a list of all factors
                 that are raised to an odd power (2 and 8 are 2, 4 is not used)
        """
        retv = []
        lval = value
        for i in self.plist:
            cnt = 0
            while lval % i == 0:
                lval /= i
                cnt += 1
            if cnt % 2 != 0:
                retv.append(i)
        if lval > self.limit:
            retv.append(lval)
        return retv

    def getpSols(self):
        """
        Initialize self.solutions.  Self.solutions is a dictionary indexed
        by numbers p^n where p is a prime number, n is a positive integer, and
        p^n is less than 8000.  The values are the prime factors of the divisor
        sum square list returned from findSol.
        """
        self.solutions = {}
        for i in self.plist:
            value = 1 + i*i
            j = i
            while j < self.limit:
                self.solutions[j] = self.findSol(value)
                j = j*i
                value += j*j

    def setLower(self):
        """
        First set first8k, a list of divisor sum squares lists for the
        first 8000 integers.  Next intialize self.lowhist, a dictionary
        of valid numbers that can be multiplied by a number greater
        than 8000 to form a number with a divisor sum square that is a n^2.
        The values of each dictionary entry are numbers in the range 1-8000
        the product of whose divisor sum squares equals the index of the
        entry (excluding internal integer powers that are factored out).
        """
        def get_first_8k():
            first8k = self.limit * [[]]
            for i, val in self.solutions.items():
                first8k[i] = val[::]
            return first8k
        first8k = get_first_8k()
        for i in range(2, self.limit):
            if len(first8k[i]) == 0:
                temp = i
                finished = False
                loop = iter(self.plist)
                while not finished:
                    j = next(loop)
                    fact = 1
                    while temp % j == 0:
                        fact *= j
                        temp //= j
                    if fact > 1:
                        xvec = addVecs(first8k[fact], first8k[temp])
                        first8k[i] = xvec
                        finished = True
        self.lowhist = {}
        for i in range(2, self.limit):
            prod = 1
            bad = False
            for j in first8k[i]:
                if j % 2 == 1:
                    if not j % 4 == 1:
                        bad = True
                        break
                prod *= j
            if bad:
                continue
            if prod not in self.lowhist:
                self.lowhist[prod] = [i]
            else:
                self.lowhist[prod].append(i)

    def polNums(self):
        """
        Intialize self.hist, a dictionary indexed by numbers in the range
        2-8000.  Each value is the number of times that index number appears
        in self.solutions.
        """
        self.hist = {}
        for val in self.solutions.values():
            for numb in val:
                if numb in self.hist:
                    self.hist[numb] += 1
                else:
                    self.hist[numb] = 1

    def getSame(self, i, count):
        """
        Scan the self.solutions dictionary and return the first count
        (third parameter) entries that contain i (second parameter).
        """
        proda = []
        loop = iter(self.solutions)
        while len(proda) != count:
            j = next(loop)
            if i in self.solutions[j]:
                proda.append(j)
        return proda

    def reducev(self, vector):
        """
        The input vector is a list of self.solutions keys.  Each key is
        combined with every other key and a new self.solutions value is
        created if this combination is valid.  Then all entries in vector
        are deleted from self.solutions.
        """
        for ii in range(0, len(vector)-1):
            for jj in range(ii+1, len(vector)):
                i = vector[ii]
                j = vector[jj]
                if gcd(j, i) != 1:
                    continue
                newi = i*j
                if newi < self.biglimit:
                    nvec = addVecs(self.solutions[i], self.solutions[j])
                    self.solutions[newi] = nvec
        for i in vector:
            del self.solutions[i]


def main():
    """
    Main entry point.
    """
    prob = problem211(64000000)
    answer = prob.doit()
    return answer
