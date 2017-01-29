/**
 * 
 */
package projectEuler.challenge150;

import java.util.List;

import projectEuler.utilities.factories.ListFactory;

/**
 * @author matt
 *
 */
public class ArrayChallengeTriangle implements Triangle {
	
	public ArrayChallengeTriangle(ListFactory listFactory) {
		this.sums = listFactory.createList();
		
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
				
				sums.add(total);
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
		
		final int rowIndex = ((row + 1) * row) / 2;
		
		final int rightHandSideIndex = beginIndex + length - 1 + rowIndex;
		final int rightHandSum = sums.get(rightHandSideIndex);
		
		if(beginIndex == 0) {
			return rightHandSum;
		} else {
			final int leftHandSideIndex = beginIndex - 1 + rowIndex;
			
			final int leftHandSum = sums.get(leftHandSideIndex);

			final int total = rightHandSum - leftHandSum;
		
			return total;
		}
	}
	
	private final List<Integer> sums;
	private final int numRows = 1000;

}
