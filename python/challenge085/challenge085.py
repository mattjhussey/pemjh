def numRects(h, w):
    # w types per h
    count = 0
    for rh in xrange(1, h + 1):
        for rw in xrange(1, w + 1):
            numAcross = w - rw + 1
            numDown = h - rh + 1
            count += numAcross * numDown

    return count

def challenge085():
    width = 1
    target = 2000000
    closest = target # ie 0
    area = 0
    while True:
        # Get rectangles for width 1
        rectangles = numRects(1, width)
        # If greater than 2 million and further away than closest
        if rectangles > target and abs(target - rectangles) > closest:
            # Will never improve
            break
        else:
            # use triangle numbers to find the closest to 2000000
            triangle = 0
            height = 1
            while True:
                triangle += height
                
                # Get difference
                areaRectangles = rectangles * triangle
                difference = abs(target - areaRectangles)
            
                if difference < closest:
                    closest = difference
                    area = width * height

                if areaRectangles > target:
                    break # Cannot improve

                height += 1

        width += 1

    return area

answer = 2772

if __name__ == "__main__":
    print challenge085()
