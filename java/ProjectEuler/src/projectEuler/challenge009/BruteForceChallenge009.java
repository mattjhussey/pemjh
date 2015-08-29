/**
 * 
 */
package projectEuler.challenge009;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge009 implements Challenge009 {

	/* (non-Javadoc)
	 * @see projectEuler.challenge009.Challenge009#findProductTripletWhereSumIsN(int)
	 */
	@Override
	public int findProductTripletWhereSumIsN(int n) {
		
		int highestProduct = 0;
		// a + b + c = n
		// a < b < c
		// a^2 + b^2 - c^2 = 0
		// a cannot be equal to or greater than half of n else there is no room for b and c
		final int halfN = n / 2;
		for(int a = 1; a != halfN; ++a) {
			final int aSquared = a * a;
			
			// Of the remainder, b cannot be equal to or greater than half of n else there is no room for b and c
			final int remainder = n - a;
			final int halfRemainder = remainder / 2;
			final int bLimit = a + halfRemainder;
			final int startB = a + 1;
			for(int b = startB; b != bLimit; ++b) {
				final int c = n - a - b;
				
				final int bSquared = b * b;
				final int cSquared = c * c;
				
				final int equated = aSquared + bSquared - cSquared; 
				if(equated == 0) {
					// Triplet found
					final int product = a * b * c;
					
					if(product > highestProduct) {
						highestProduct = product;
					}
				}
			}
		}
		
		return highestProduct;
	}

}
