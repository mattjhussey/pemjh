/**
 * 
 */
package projectEuler.challenge008;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge008 implements Challenge008 {

	/* (non-Javadoc)
	 * @see projectEuler.challenge008.Challenge008#findHighest5DigitProduct(java.lang.String)
	 */
	@Override
	public int findHighest5DigitProduct(String numString) {
		final int limit = numString.length() - 4;
		
		int highest = Integer.MIN_VALUE;
		
		for(int index = 0; index != limit; ++index) {
			String next5 = numString.substring(index, index + 5);
			
			int value = 1;
			for(char c: next5.toCharArray()) {
				int i = (int)c - 48;
				value *= i;
			}
			
			if(value > highest) {
				highest = value;
			}
		}
		
		return highest;
	}

}
