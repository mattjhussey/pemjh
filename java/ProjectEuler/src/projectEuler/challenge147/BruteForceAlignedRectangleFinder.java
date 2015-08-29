/**
 * 
 */
package projectEuler.challenge147;

/**
 * @author matt
 *
 */
public class BruteForceAlignedRectangleFinder implements AlignedRectangleFinder {

	/* (non-Javadoc)
	 * @see projectEuler.challenge147.AlignedRectangleFinder#findNumberOfRectanglesInMN(int, int)
	 */
	@Override
	public int findNumberOfRectanglesInMN(int m, int n) {
		int total = 0;
		
		// Work out horizontal rectangle shapes i, j (for totalling and recursive calls)
		final int mLimit = m + 1;
		final int nLimit = n + 1;
		for(int i = 1; i != mLimit; ++i) {
			for(int j = 1; j != nLimit; ++j) {
				// How many times does it fit horizontally?
				final int horizontal = m - i + 1;
				// How many times does it fit vertically?
				final int vertical = n - j + 1;
				// Therefore, how many times does it fit? (horizontal * vertical)
				final long rectanglesThisLevel = horizontal * vertical;
				
				// Get i, j rectangle total (recursive)
				// How many rectangles total? horizontal * vertical + recursive * horizontal * vertical
				
				total += rectanglesThisLevel;
			}
		}
		
		return total;
	}

}
