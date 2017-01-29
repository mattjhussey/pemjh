/**
 * 
 */
package projectEuler.challenge150;

import java.util.Map;

import projectEuler.utilities.factories.MapFactory;

/**
 * @author matt
 *
 */
public class TestTriangle implements Triangle {
	
	public TestTriangle(MapFactory mapFactory, CoordinateFactory coordinateFactory) {
		sums = mapFactory.createMap();
		this.coordinateFactory = coordinateFactory;
		
		// Row 0
		// 15
		sums.put(coordinateFactory.createCoordinate(0, 0), 15);
		
		// Row 1
		// -14
		sums.put(coordinateFactory.createCoordinate(1, 0), -14);
		// -7
		sums.put(coordinateFactory.createCoordinate(1, 1), -21);
		
		// Row 2
		// 20
		sums.put(coordinateFactory.createCoordinate(2, 0), 20);
		// -13
		sums.put(coordinateFactory.createCoordinate(2, 1), 7);
		// -5
		sums.put(coordinateFactory.createCoordinate(2, 2), 2);
		
		// Row 3
		// -3
		sums.put(coordinateFactory.createCoordinate(3, 0), -3);
		// 8
		sums.put(coordinateFactory.createCoordinate(3, 1), 5);
		// 23
		sums.put(coordinateFactory.createCoordinate(3, 2), 28);
		// -26
		sums.put(coordinateFactory.createCoordinate(3, 3), 2);
		
		// Row 4
		// 1
		sums.put(coordinateFactory.createCoordinate(4, 0), 1);
		// -4
		sums.put(coordinateFactory.createCoordinate(4, 1), -3);
		// -5
		sums.put(coordinateFactory.createCoordinate(4, 2), -8);
		// -18
		sums.put(coordinateFactory.createCoordinate(4, 3), -26);
		// 5
		sums.put(coordinateFactory.createCoordinate(4, 4), -21);
		
		// Row 5
		// -16
		sums.put(coordinateFactory.createCoordinate(5, 0), -16);
		// 31
		sums.put(coordinateFactory.createCoordinate(5, 1), 15);
		// 2
		sums.put(coordinateFactory.createCoordinate(5, 2), 17);
		// 9
		sums.put(coordinateFactory.createCoordinate(5, 3), 26);
		// 28
		sums.put(coordinateFactory.createCoordinate(5, 4), 54);
		// 3
		sums.put(coordinateFactory.createCoordinate(5, 5), 57);
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge150.Triangle#getRows()
	 */
	@Override
	public int getRows() {
		return 6;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge150.Triangle#getSum(int, int, int)
	 */
	@Override
	public int getSum(int row, int beginIndex, int length) {
		if((row < 0) || (row >= getRows())) {
			throw new IllegalArgumentException("Row out of range");
		}
		if(length < 1) {
			throw new IllegalArgumentException("Length must be greater than 0");
		}
		if((beginIndex < 0) || (beginIndex > row)) {
			throw new IllegalArgumentException("BeginIndex is out of range");
		}
		if((beginIndex + length) > (row + 1)) {
			throw new IllegalArgumentException("BeginIndex + Length goes out of range");
		}
		
		final int rightHandSideIndex = beginIndex + length - 1;
		final Coordinate rightCoordinate = coordinateFactory.createCoordinate(row, rightHandSideIndex);
		final int rightHandSum = sums.get(rightCoordinate);
		
		if(beginIndex == 0) {
			return rightHandSum;
		} else {
			final int leftHandSideIndex = beginIndex - 1;
			
			final Coordinate leftCoordinate = coordinateFactory.createCoordinate(row, leftHandSideIndex);
			final int leftHandSum = sums.get(leftCoordinate);
			
			final int total = rightHandSum - leftHandSum;
		
			return total;
		}
	}
	
	private final Map<Coordinate, Integer> sums;
	private final CoordinateFactory coordinateFactory;

}