/**
 * 
 */
package projectEuler.challenge140;

import java.util.List;

import projectEuler.utilities.factories.ListFactory;

/**
 * @author matt
 *
 */
public final class BruteForceGoldenNuggetGenerator implements GoldenNuggetGenerator {
	
	public BruteForceGoldenNuggetGenerator(ListFactory listFactory, FibonacciGenerator fibonacciGenerator) {
		this.listFactory = listFactory;
		this.fibonacciGenerator = fibonacciGenerator;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge140.GoldenNuggetGenerator#generateNGoldenNuggets(int)
	 */
	@Override
	public List<Long> generateNGoldenNuggets(int n) {
		
		List<Long> list = listFactory.createList();
		
		int remaining = n;
		
		// Need 2 for each of n, except the first
		final int fibsNeeded = 2 * n - 1;
		
		final List<Long> fibs = fibonacciGenerator.generateNFibonacciNumbers(fibsNeeded);
		
		boolean doubleUp = true;
		 
		int fibIndex = 0;
		
		// Begin at 0 because the first step should inc us twice by 1 to become 2
		long current = 0;
		
		while(remaining > 0) {
			
			final long fib = fibs.get(fibIndex);
			
			// Skip 2 fibs next time
			fibIndex += 2;
			
			current += fib;
			
			if(doubleUp) {
				current += fib;
			}
			
			doubleUp = !doubleUp;
			
			list.add(current);
			
			--remaining;
		}
		
		return list;
	}
	
	private final ListFactory listFactory;
	private final FibonacciGenerator fibonacciGenerator;

}
