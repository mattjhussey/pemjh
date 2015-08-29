/**
 * 
 */
package projectEuler.challenge005;

import java.util.Map;
import java.util.Map.Entry;

import projectEuler.utilities.factories.MapFactory;
import projectEuler.utilities.maths.PrimeGenerator;

/**
 * @author matt
 *
 */
public final class PrimeFactorChallenge005 implements Challenge005 {
	
	public PrimeFactorChallenge005(PrimeGenerator primeGenerator, MapFactory mapFactory) {
		this.primeGenerator = primeGenerator;
		this.mapFactory = mapFactory;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge005.Challenge005#findLowestCommonDenominatorOfNumsUpToN(int)
	 */
	@Override
	public int findLowestCommonDenominatorOfNumsUpToN(int n) {
		// All primes up to and including n will be needed
		final Iterable<Integer> primes = primeGenerator.findPrimesUpToN(n);
		
		// Create a map of primes and counts
		final Map<Integer, Integer> primeCounts = mapFactory.createMap();
		for(Integer prime: primes) {
			primeCounts.put(prime, 0);
		}
		
		// Loop through each number and work out the size of the factors needed. Record these if they are larger than any previously used.
		final int maximum = n + 1;
		for(int i = 1; i != maximum; ++i) {
			int remaining = i;
			
			for(Integer prime: primes) {
				
				if(remaining == 1) {
					// No more factors
					break;
				}
				
				int numDivs = 0;
				while((remaining % prime) == 0) {
					// Divides
					++numDivs;
					remaining /= prime;
				}
				
				if(numDivs > 0) {
					int existingDivs = primeCounts.get(prime);
					
					if(numDivs > existingDivs) {
						primeCounts.put(prime, numDivs);
					}
				}
			}
		}
		
		// Multiply up all the primes
		int lcd = 1;
		for(Entry<Integer, Integer> factor: primeCounts.entrySet()) {
			Integer value = factor.getValue();
			if(value > 0) {
				Integer prime = factor.getKey();
				lcd *= Math.pow(prime, value);
			}
		}
		
		return lcd;
	}
	
	private final PrimeGenerator primeGenerator;
	private final MapFactory mapFactory;

}
