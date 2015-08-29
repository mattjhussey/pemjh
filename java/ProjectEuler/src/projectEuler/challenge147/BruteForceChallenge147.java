/**
 * 
 */
package projectEuler.challenge147;

/**
 * @author matt
 *
 */
public class BruteForceChallenge147 implements Challenge147 {
	
	public BruteForceChallenge147(AlignedRectangleFinder alignedRectangleFinder, DiagonalRectangleFinder diagonalRectangleFinder) {
		this.alignedRectangleFinder = alignedRectangleFinder;
		this.diagonalRectangleFinder = diagonalRectangleFinder;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge147.Challenge147#findTotalRectanglesInGridsMNAndSmaller(int, int)
	 */
	@Override
	public long findTotalRectanglesInGridsMNAndSmaller(int m, int n) {
		long total = 0;
		
		// Work out horizontal rectangle shapes i, j (for totalling and recursive calls)
		final int mLimit = m + 1;
		final int nLimit = n + 1;
		for(int i = 1; i != mLimit; ++i) {
			for(int j = 1; j != nLimit; ++j) {
				final long alignedRectangles = alignedRectangleFinder.findNumberOfRectanglesInMN(i, j);
				final long diagonalRectangles = diagonalRectangleFinder.findNumberOfRectanglesInMN(i, j);
				final long rectangles = alignedRectangles + diagonalRectangles;
				total += rectangles;
			}
		}		 
		
		return total;
	}
	
	private final AlignedRectangleFinder alignedRectangleFinder;
	private final DiagonalRectangleFinder diagonalRectangleFinder;

}
