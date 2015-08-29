def isLeapYear(y):
    return ((not y % 100) and (not y % 400)) or \
        ((y % 100) and (not y % 4))

def getYearDays(y):
    if isLeapYear(y):
        return 366
    else:
        return 365

def getFirstJan(y):
    totalDays = 1
    for i in xrange(1900, y):
        totalDays += getYearDays(i)
    return totalDays % 7

def monthStartDays(y):
    # Get the 1st of january
    day = getFirstJan(y)
    monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    if isLeapYear(y):
        monthLengths[1] = 29

    yield day
    for m in monthLengths:
        day += m
        day = day % 7
        yield day

def challenge019():

    # Loop through years
    totalDays = 0
    for y in xrange(1901, 2001):
        # Loop through the first days of the months for the year
        for d in monthStartDays(y):
            if d == 0:
                totalDays += 1

    return totalDays

answer = 171

if __name__ == "__main__":
    import sys
    print challenge019()
