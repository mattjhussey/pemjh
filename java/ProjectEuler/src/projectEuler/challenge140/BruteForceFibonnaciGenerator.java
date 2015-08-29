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
public final class BruteForceFibonnaciGenerator implements FibonacciGenerator {
	
	public BruteForceFibonnaciGenerator(ListFactory listFactory) {
		this.listFactory = listFactory;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge140.FibonacciGenerator#generateNFibonacciNumbers(int)
	 */
	@Override
	public List<Long> generateNFibonacciNumbers(int n) {
		List<Long> list = listFactory.createList();
		
		long fibo1 = 0;
		long fibo2 = 1;
		
		int remaining = n;
		
		while(remaining > 0) {
			
			fibo2 += fibo1;
			fibo1 = fibo2 - fibo1;
			
			list.add(fibo2);
			
			--remaining;
		}
		
		return list;
	}
	
	private final ListFactory listFactory;

}
