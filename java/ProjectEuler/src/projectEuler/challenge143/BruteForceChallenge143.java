/**
 * 
 */
package projectEuler.challenge143;

import java.util.Set;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge143 implements Challenge143 {
	
	public BruteForceChallenge143(UniqueFermatPointLengthFinder lengthFinder) {
		this.lengthFinder = lengthFinder;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge143.Challenge143#findFermatPointSumsUpToN(int)
	 */
	@Override
	public long findFermatPointSumsUpToN(int n) {
		
		Set<Integer> results = lengthFinder.findUniqueFermatPointLengthsUpToN(n);
		
		long total = 0;
		
		for(Integer result: results) {
			total += result;
		}
		return total;
	}
	
	private final UniqueFermatPointLengthFinder lengthFinder;

}
