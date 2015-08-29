/**
 * 
 */
package projectEuler.challenge141;

import java.util.Set;

import projectEuler.utilities.factories.SetFactory;
/**
 * @author matt
 *
 */
public final class CFirstCutDownChallenge141 implements Challenge141 {
	
	public CFirstCutDownChallenge141(SetFactory setFactory) {
		this.setFactory = setFactory;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge141.Challenge141#findSumOfProgressiveSquaresBelowN(long)
	 */
	@Override
	public long findSumOfProgressiveSquaresBelowN(long n) {
		
		// 97344 312 8 92 1058 92 1058 8
		
		Set<Long> squares = setFactory.createSet();
		
		final long aLimit = (long) Math.pow(n, 0.5) + 1;
		
		final long cLimit = (long) Math.pow(aLimit, 0.5);
		
		for(long c = 1; c != cLimit; ++c) {
			final long c2 = c * c;
			final long c3 = c * c * c;
			
			final long aMultipleLimit = aLimit / c2;
			
			assert aMultipleLimit > 0 : "aMultiple should be more than 0";
			
			for(long aMultiple = 1; aMultiple != aMultipleLimit; ++aMultiple) {
				final long a = c2 * aMultiple;
				final long a2 = a * a;				

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
									
									squares.add(value);
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
	
	private final SetFactory setFactory;

}
