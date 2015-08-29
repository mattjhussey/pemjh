/**
 * 
 */
package projectEuler.challenge010;

import java.util.SortedSet;

import projectEuler.utilities.maths.PrimeGenerator;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge010 implements Challenge010 {
	
	public BruteForceChallenge010(PrimeGenerator primeGenerator) {
		this.primeGenerator = primeGenerator;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge010.Challenge010#findSumOfAllPrimesUpToN(int)
	 */
	@Override
	public long findSumOfAllPrimesUpToN(int n) {
		SortedSet<Integer> primes = primeGenerator.findPrimesUpToN(n);
		
		long sum = 0;
		for(int prime: primes) {
			sum += prime;
		}
		
		return sum;
	}
	
	private final PrimeGenerator primeGenerator;

}
