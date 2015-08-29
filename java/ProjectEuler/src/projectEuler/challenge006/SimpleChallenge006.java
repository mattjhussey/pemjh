/**
 * 
 */
package projectEuler.challenge006;

/**
 * @author matt
 *
 */
public final class SimpleChallenge006 implements Challenge006 {
	
	public SimpleChallenge006(SumFinder sumFinder, SumOfSquaresFinder sumOfSquaresFinder) {
		this.sumFinder = sumFinder;
		this.sumOfSquaresFinder = sumOfSquaresFinder;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge006.Challenge006#findDifferenceBetweenSqSumAndSumSq(int)
	 */
	@Override
	public int findDifferenceBetweenSqSumAndSumSq(int n) {
		int sum = sumFinder.findSumUpToN(n);
		int squareOfSum = sum * sum;
		
		int sumOfSquares = sumOfSquaresFinder.findSumOfSquaresUpToN(n);
		
		int difference = squareOfSum - sumOfSquares;
		
		int absoluteDifference = Math.abs(difference);
		
		return absoluteDifference;
	}
	
	private final SumFinder sumFinder;
	private final SumOfSquaresFinder sumOfSquaresFinder;

}
