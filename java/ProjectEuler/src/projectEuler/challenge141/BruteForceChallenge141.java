/**
 * 
 */
package projectEuler.challenge141;

import java.util.Iterator;
import java.util.SortedSet;
import java.util.TreeSet;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge141 implements Challenge141 {

	/* (non-Javadoc)
	 * @see projectEuler.challenge141.Challenge141#findSumOfProgressiveSquaresBelowN(long)
	 */
	@Override
	public long findSumOfProgressiveSquaresBelowN(long n) {
		
		long total = 0;
		
		// Only look at squares...
		final long rootLimit = (long) Math.sqrt(n) + 1;
		
		for(long root = 2; root != rootLimit; ++root) {
			final long square = root * root;
			
			final long dLimit = root + 1;
			for(long d = 1; d != dLimit; ++d) {
				final long q = square / d;
				final long r = square % d;
				
				if((q == 0) || (r == 0) || (d == q) || (d == r) || (q == r)) {
					// Won't work
				} else {				
					final SortedSet<Long> sorted = new TreeSet<>();
					sorted.add(d);
					sorted.add(q);
					sorted.add(r);
					
					final Iterator<Long> nums = sorted.iterator();
					final long n1 = nums.next();
					final long n2 = nums.next();
					// d = n2 / n1
					final long predictedN3Numerator = n2 * n2;
					if((predictedN3Numerator % n1) == 0) {
						final long predictedN3 = predictedN3Numerator / n1;
						final long n3 = nums.next();
						
						if(n3 == predictedN3) {
							total += square;
							break;
						}
					}
				}
			}
		}
		
		return total;
	}

}
