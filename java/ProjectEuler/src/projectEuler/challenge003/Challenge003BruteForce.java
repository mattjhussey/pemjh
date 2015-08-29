/**
 * 
 */
package projectEuler.challenge003;

/**
 * @author matt
 *
 */
public final class Challenge003BruteForce implements Challenge003 {

	/* (non-Javadoc)
	 * @see projectEuler.challenge003.Challenge003#getLargestPrimeFactor(int)
	 */
	@Override
	public long getLargestPrimeFactor(long n) {
		long target = n;

		// Begin at 1 (will increment to 2 on first loop)
		int divisor = 1;
		
		while(target != 1) {
			++divisor;
			
			while ((target % divisor) == 0) {
				// Divisor goes into target so reduce target
				target /= divisor;
			}
		}
		
		return divisor;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
