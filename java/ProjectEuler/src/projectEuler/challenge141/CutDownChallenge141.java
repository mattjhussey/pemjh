/**
 * 
 */
package projectEuler.challenge141;

import java.util.Set;
import java.util.SortedSet;

import projectEuler.utilities.factories.SetFactory;
import projectEuler.utilities.maths.PrimeGenerator;

/**
 * @author matt
 *
 */
public final class CutDownChallenge141 implements Challenge141 {
	
	public CutDownChallenge141(PrimeGenerator generator, SetFactory setFactory) {
		this.generator = generator;
		this.setFactory = setFactory;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge141.Challenge141#findSumOfProgressiveSquaresBelowN(long)
	 */
	@Override
	public long findSumOfProgressiveSquaresBelowN(long n) {
		
		// 97344 312 8 92 1058 92 1058 8
		
		Set<Long> squares = setFactory.createSet();
		
		final long aLimit = (long) Math.sqrt(n) + 1;
		
		SortedSet<Integer> primes = generator.findPrimesUpToN((int) aLimit);
		primes.add(1);
		
		for(long a = 1; a != aLimit; ++a) {
			if((a != 1) && primes.contains((int) a)) {
				
			} else {
				// C must be 1 or divide a
				// C^3 must be less than or equal to a (I think just less than)
				final long a2 = a * a;
				for(long c = 1, c3 = c * c * c; c3 <= a2; ++c, c3 = c * c * c) {
					final boolean dividesA = ((a % (c * c)) == 0) && ((c3 == 1) || (c3 != a2));
					
					if(dividesA) {
						final long acFactor = a2 / c3;
						
						// Find b, which should not be divisible by c
						final long maximumB = (n - a) / acFactor + 1;
						// b should be greater than c
						final long minimumB = c + 1;
						if(minimumB <= maximumB) {
							for(long b = minimumB, b3 = b * b * b; b3 < maximumB; ++b, b3 = b * b * b) {
								final boolean dividesByC = (c != 1) && ((b % c) == 0);
								
								if(!dividesByC) {
									final long value = acFactor * b3 + a;									
									
									long root = (long) Math.sqrt(value);
									long rebuilt = root * root;
									if(rebuilt == value) {
										// Checking...
										final long dNum = a * b;
										final boolean divsByC = (dNum % c) == 0;
										assert divsByC : "Should divide by C";
										final long d = dNum / c;
										final long qNum = d * b;
										final boolean divsByC2 = (qNum % c) == 0;
										assert divsByC2 : "Should divide by C (2)";
										final long q = qNum / c;
										final long check = d * q + a;
										assert value == check : "Should be the same";
										
										//System.out.println(String.format("%d %d %d %d", a, b, c, value));
										squares.add(value);
									} 
								}
							}
						}
					}
				}
			}
		}
		
		long total = 0;
		
		for(Long value: squares) {
			if (value == 1630544400) {
				System.out.println("Here");
			}
			total += value;
		}
		
		return total;
	}
		
	private final PrimeGenerator generator;
	private final SetFactory setFactory;

}
