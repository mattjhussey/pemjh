def challenge006():
    max = 100

    sumOfSquares = 0
    # Find the sum of the squares
    for i in range(1, max + 1):
        sumOfSquares += i**2

    # Find the sum
    sum = (max * (max + 1)) / 2
    
    # Find the square
    squareOfSums = sum**2

    # Find the difference
    difference = abs(squareOfSums - sumOfSquares)
    
    return difference

answer = 25164150

if __name__ == "__main__":
    import sys
    print challenge006()
