/**
 * 
 */
package projectEuler.challenge006;

/**
 * @author matt
 *
 */
public final class ClosedFunctionSumFinder implements SumFinder {

	/* (non-Javadoc)
	 * @see projectEuler.challenge006.SumFinder#findSumUpToN(int)
	 */
	@Override
	public int findSumUpToN(int n) {
		final int sum = n * (n + 1) / 2;
		return sum;
	}

}
