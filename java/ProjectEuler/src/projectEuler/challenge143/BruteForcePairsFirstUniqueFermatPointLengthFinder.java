/**
 * 
 */
package projectEuler.challenge143;

import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import projectEuler.utilities.factories.SetFactory;

/**
 * @author matt
 *
 */
public class BruteForcePairsFirstUniqueFermatPointLengthFinder implements
		UniqueFermatPointLengthFinder {
	
	public BruteForcePairsFirstUniqueFermatPointLengthFinder(Triangle120PairFinder pairFinder, SetFactory setFactory) {
		this.pairFinder = pairFinder;
		this.setFactory = setFactory;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge143.UniqueFermatPointLengthFinder#findUniqueFermatPointLengthsUpToN(int)
	 */
	@Override
	public Set<Integer> findUniqueFermatPointLengthsUpToN(int n) {
		
		Map<Integer, Set<Integer>> pairs = pairFinder.findPairsOfSidesLessThanN(n);
		
		Set<Integer> results = setFactory.createSet();
		
		// Build triangles, loop through triangles
		for(Entry<Integer, Set<Integer>> pair: pairs.entrySet()) {
			final int p = pair.getKey();			
			// Get each paired value
			for(Integer q: pair.getValue()) {
				final long ql = (long) q;
				
				final int pq = p + q;
				if(pq < n) {
					// P is the shortest currently so use that for find r
					for(Integer r: pair.getValue()) {
						final int total = pq + r;
						
						if(total <= n) {
							final long rl = (long) r;
							// Check that q and r are paired
							final long c = ql*ql + ql*rl + rl*rl;
							
							final long root = (long) Math.sqrt(c);
							
							final long rebuilt = root * root;
							if(rebuilt == c) {
								results.add(total);								
							}
						}
					}
				}
			}
		}
		
		return results;
	}
	
	private final Triangle120PairFinder pairFinder;
	private final SetFactory setFactory;

}
