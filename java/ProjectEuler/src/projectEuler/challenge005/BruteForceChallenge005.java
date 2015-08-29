/**
 * 
 */
package projectEuler.challenge005;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge005 implements Challenge005 {

	/* (non-Javadoc)
	 * @see projectEuler.challenge005.Challenge005#findLowestCommonDenominatorOfNumsUpToN(int)
	 */
	@Override
	public int findLowestCommonDenominatorOfNumsUpToN(int n) {
		
		final int maximum = n + 1;
		
		int possibleAnswer = n;
		
		while(true) {
			boolean success = true;
			
			for(int divisor = 1; divisor != maximum; ++divisor) {
				final int remainder = possibleAnswer % divisor;
				if(remainder != 0) {
					success = false;
					break;
				}
			}
			
			if(success) {
				return possibleAnswer;
			}
			
			++possibleAnswer;
		}
	}
	
	public static void main(String[] args) {
		System.out.println((new BruteForceChallenge005()).findLowestCommonDenominatorOfNumsUpToN(20));
	}

}
