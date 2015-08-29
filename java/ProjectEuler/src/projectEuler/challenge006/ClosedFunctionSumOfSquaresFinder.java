/**
 * 
 */
package projectEuler.challenge006;

/**
 * @author matt
 *
 */
public final class ClosedFunctionSumOfSquaresFinder implements SumOfSquaresFinder {

	/* (non-Javadoc)
	 * @see projectEuler.challenge006.SumOfSquaresFinder#findSumOfSquaresUpToN(int)
	 */
	@Override
	public int findSumOfSquaresUpToN(int n) {
		final int sum = n * (n + 1) * (2 * n + 1) / 6;
		return sum;
	}

}
