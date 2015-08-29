/**
 * 
 */
package projectEuler.challenge002;

/**
 * @author matt
 *
 */
public final class Challenge002BruteForce implements Challenge002 {

	/* (non-Javadoc)
	 * @see projectEuler.challenge002.Challenge002#getFibonacciSum(int)
	 */
	@Override
	public int getFibonacciSum(int limit) {
		int a = 1;
		int b = 1;
		int total = 0;
		
		while(b < limit) {
			boolean isEven = (b % 2) == 0;
			if(isEven) {
				total += b;
			}
			b += a;
			a = b - a;
		}
		
		return total;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
