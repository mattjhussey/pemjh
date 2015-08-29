/**
 * 
 */
package projectEuler.challenge007;

import java.util.Iterator;
import java.util.SortedSet;

import projectEuler.utilities.factories.SortedSetFactory;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge007 implements Challenge007 {
	
	public BruteForceChallenge007(SortedSetFactory sortedSetFactory) {
		this.sortedSetFactory = sortedSetFactory;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge007.Challenge007#findNthPrime(int)
	 */
	@Override
	public int findNthPrime(int n) {
		
		final int indexN = n - 1;
		
		// Set up known primes
		final SortedSet<Integer> primes = sortedSetFactory.createSortedSet();
		primes.add(2);
		primes.add(3);
		primes.add(5);
		
		if(n > 3) {
			
			// Next prime to check
			int current = 7;
			
			while(primes.size() < n) {
				final int maxFactor = (int) Math.sqrt(current);
				
				boolean factorFound = false;
				
				for(Integer factor: primes) {
					if(factor > maxFactor) {
						break;
					}
					
					if((current % factor) == 0) {
						// Not a prime, factor found
						factorFound = true;
						break;
					}
				}
				
				if(!factorFound) {
					primes.add(current);
				}
				
				current += 2;
				
			}
		}

		Iterator<Integer> iterator = primes.iterator();
		
		int index = 0;
		
		while(index != indexN) {
			iterator.next();
			++index;
		}
		
		return iterator.next();
	}
	
	private final SortedSetFactory sortedSetFactory;

}
