def getNumberLength(n, known, hundredRep, andRep, thousandRep):
    if n == 1000:
        return thousandRep
    else:
        tempN = n

        numberRepresentation = known[0]
        # If over one hundred then print the hundred section
        if tempN > 99:
            # Get the hundreds
            hundreds = tempN / 100
            # Add the hundreds string
            numberRepresentation += known[hundreds] + hundredRep
            # Add "and" if the number is not an exact hundred
            if (tempN % 100):
                numberRepresentation += andRep
            # Remove the hundreds column for later processing
            tempN -= (hundreds * 100)

        # Is remainder already known
        if known.has_key(tempN):
            numberRepresentation += known[tempN]
        else:
            # If over 19 print the tens
            if tempN > 19:
                # Get the tens
                tens = tempN / 10
                # Remove the tens column for later processing
                tempN -= (tens * 10)
                # Add the tens string
                numberRepresentation += known[tens * 10]
        
            # If less than 20, or not divisible but 10 then print singles
            if (tempN < 20) and (tempN != 0):
                numberRepresentation += known[tempN]

    known[n] = numberRepresentation    

    return numberRepresentation

def challenge017():
    known = {0: "", \
                 1: "one", \
                 2: "two", \
                 3: "three", \
                 4: "four", \
                 5: "five", \
                 6: "six", \
                 7: "seven", \
                 8: "eight", \
                 9: "nine", \
                 10: "ten", \
                 11: "eleven", \
                 12: "twelve", \
                 13: "thirteen", \
                 14: "fourteen", \
                 15: "fifteen", \
                 16: "sixteen", \
                 17: "seventeen", \
                 18: "eighteen", \
                 19: "nineteen", \
                 20: "twenty", \
                 30: "thirty", \
                 40: "forty", \
                 50: "fifty", \
                 60: "sixty", \
                 70: "seventy", \
                 80: "eighty", \
                 90: "ninety"}
    knownInts = {0: 0, \
                 1: 3, \
                 2: 3, \
                 3: 5, \
                 4: 4, \
                 5: 4, \
                 6: 3, \
                 7: 5, \
                 8: 5, \
                 9: 4, \
                 10: 3, \
                 11: 6, \
                 12: 6, \
                 13: 8, \
                 14: 8, \
                 15: 7, \
                 16: 7, \
                 17: 9, \
                 18: 8, \
                 19: 8, \
                 20: 6, \
                 30: 6, \
                 40: 5, \
                 50: 5, \
                 60: 5, \
                 70: 7, \
                 80: 6, \
                 90: 6}

    complete = ""
    endLine = 0
    for i in range(1, 1001):
        complete += getNumberLength(i, known, 'hundred', 'and', 'onethousand')
        
    return len(complete)

answer = 21124

if __name__ == "__main__":
    import sys
    print challenge017()
