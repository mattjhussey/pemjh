/**
 * 
 */
package projectEuler.challenge143;

import java.util.Set;

import projectEuler.utilities.factories.SetFactory;

/**
 * @author matt
 *
 */
public class BruteForceUniqueFermatPointLengthFinder implements
		UniqueFermatPointLengthFinder {
	
	public BruteForceUniqueFermatPointLengthFinder(SetFactory setFactory, Triangle120SideVerifier verifier) {
		this.setFactory = setFactory;
		this.verifier = verifier;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge143.UniqueFermatPointLengthFinder#findUniqueFermatPointLengthsUpToN(int)
	 */
	@Override
	public Set<Integer> findUniqueFermatPointLengthsUpToN(int n) {
		Set<Integer> results = setFactory.createSet();

		// Find triplets (a, b, c) where a <= b <= c
		final int aLimit = n / 3 + 1;
		for(int a = 1; a != aLimit; ++a) {
			final int nRemainingA = n - a;
			final int bLimit = nRemainingA / 2 + 1;
			for(int b = a; b != bLimit; ++b) {
				
				final boolean abOk = verifier.areShortSidesOf120DegTriangle(a, b);
				
				if(abOk) {				
					final int cLimit = n - a - b + 1;
					for(int c = b; c != cLimit; ++c) {
						final int t = a + b + c;
						assert t <= n : String.format("Oops %d %d %d %d", a, b, c, t);
						
						// pair if a^2 + ab + b^2 is square
						final boolean bcOk = verifier.areShortSidesOf120DegTriangle(b, c);
						final boolean acOk = verifier.areShortSidesOf120DegTriangle(a, c);
						if(bcOk && acOk) {
							results.add(t);
						}
					}
				}
			}
		}
		
		return results;
	}
	
	private final SetFactory setFactory;
	private final Triangle120SideVerifier verifier;

}
