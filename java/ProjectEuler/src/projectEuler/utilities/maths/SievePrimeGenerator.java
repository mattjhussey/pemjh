/**
 * 
 */
package projectEuler.utilities.maths;

import java.util.List;
import java.util.SortedSet;

import projectEuler.utilities.factories.ListFactory;
import projectEuler.utilities.factories.SortedSetFactory;

/**
 * @author matt
 *
 */
public final class SievePrimeGenerator implements PrimeGenerator {
	
	public SievePrimeGenerator(ListFactory listFactory, SortedSetFactory sortedSetFactory) {
		this.listFactory = listFactory;
		this.sortedSetFactory = sortedSetFactory;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge005.PrimeGenerator#FindPrimesUpToN(int)
	 */
	@Override
	public SortedSet<Integer> findPrimesUpToN(int n) {
		// Create list of switches for the numbers [2, n]
		List<Boolean> potentialPrimes = listFactory.createList();
		
		final int maximum = n + 1;
		for(int i = 2; i != maximum; ++i) {
			potentialPrimes.add(true);
		}
		
		SortedSet<Integer> primes = sortedSetFactory.createSortedSet();

		final int maximumIndex = n - 2;
		
		// Loop through potentials
		for(int potentialPrime = 2; potentialPrime != maximum; ++potentialPrime) {
			int index = potentialPrime - 2;
			
			Boolean isPrime = potentialPrimes.get(index);
			
			if(isPrime) {
				primes.add(potentialPrime);
				
				int nonPrime = index + potentialPrime;
				while(nonPrime <= maximumIndex) {
					potentialPrimes.set(nonPrime, false);
					nonPrime += potentialPrime;
				}
			}
		}
		
		return primes;
	}
	
	private final ListFactory listFactory;
	private final SortedSetFactory sortedSetFactory;

}
