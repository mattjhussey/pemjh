/**
 * 
 */
package projectEuler.challenge001;

/**
 * @author matt
 *
 */
public final class Challenge001BruteForce implements Challenge001 {

	/* (non-Javadoc)
	 * @see projectEuler.challenge001.Challenge001#getSumOf3And5Multiples(int)
	 */
	@Override
	public final int getSumOf3And5Multiples(int limit) {
		int total = 0;
		
		for(int i = 0; i != limit; ++i) {
			boolean divsBy3 = (i % 3) == 0;
			if(divsBy3) {
				total += i;
			} else {
				boolean divsBy5 = (i % 5) == 0;
				if(divsBy5) {
					total += i;
				}
			}
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
