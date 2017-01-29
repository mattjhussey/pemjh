/**
 * 
 */
package projectEuler.challenge150;


/**
 * @author matt
 *
 */
public class BruteForceChallenge150 implements Challenge150 {

	/* (non-Javadoc)
	 * @see projectEuler.challenge150.Challenge150#findSmallestTriangleSum()
	 */
	@Override
	public int findSmallestTriangleSum(Triangle triangle) {
		final int rows = triangle.getRows();
		
		long lowestFound = Integer.MAX_VALUE;
		
		// Just move starting point to every position and add each row down
		final int headRowLimit = rows - 1;
		for(int headRowIndex = 0; headRowIndex != headRowLimit; ++headRowIndex) {
			final int valuesInHeadRow = headRowIndex + 1;
			for(int headColumnIndex = 0; headColumnIndex != valuesInHeadRow; ++headColumnIndex) {
				final int rowsRemaining = rows - headRowIndex - 1;
				
				long total = triangle.getSum(headRowIndex, headColumnIndex, 1);
				
				for(int rowStep = 0; rowStep != rowsRemaining; ++rowStep) {
					final int readRow = headRowIndex + rowStep + 1;

					final int readLength = rowStep + 2;
					
					long rowTotal = triangle.getSum(readRow, headColumnIndex, readLength);
					
					total += rowTotal;
					
					if(total < lowestFound) {
						lowestFound = total;
					}
				}
			}
		}
		
		return (int) lowestFound;
	}

}
