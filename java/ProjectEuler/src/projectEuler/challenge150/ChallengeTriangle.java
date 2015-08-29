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
public class ChallengeTriangle implements Triangle {
	
	public ChallengeTriangle(MapFactory mapFactory, CoordinateFactory coordinateFactory) {
		this.coordinateFactory = coordinateFactory;
		
		sums = mapFactory.createMap();
		
		int t = 0;
		final int _2pow20 = (int) Math.pow(2, 20);
		final int _2pow19 = (int) Math.pow(2, 19);
		final long v1 = 615949l;
		final int v2 = 797807;
		for(int rowIndex = 0; rowIndex != numRows; ++rowIndex) {
			
			final int entitiesThisRow = rowIndex + 1;
			int total = 0;
			for(int column = 0; column != entitiesThisRow; ++column) {
				final long v1t = v1 * t;
				final long lt = (v1t + v2) % _2pow20; 
				t = (int) lt;
				final int value = t - _2pow19;
				
				total += value;
				
				final Coordinate coordinate = coordinateFactory.createCoordinate(rowIndex, column);

				sums.put(coordinate, total);
			}
		}
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge150.Triangle#getRows()
	 */
	@Override
	public int getRows() {
		return numRows;
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
	
	private final int numRows = 1000;
	private final Map<Coordinate, Integer> sums;
	private final CoordinateFactory coordinateFactory;
}
