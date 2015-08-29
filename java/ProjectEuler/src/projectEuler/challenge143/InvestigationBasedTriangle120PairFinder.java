/**
 * 
 */
package projectEuler.challenge143;

import java.util.Map;
import java.util.Set;

import projectEuler.utilities.factories.MapFactory;
import projectEuler.utilities.factories.SetFactory;

/**
 * @author matt
 *
 */
public class InvestigationBasedTriangle120PairFinder implements
		Triangle120PairFinder {
	
	public InvestigationBasedTriangle120PairFinder(MapFactory mapFactory, SetFactory setFactory) {
		this.mapFactory = mapFactory;
		this.setFactory = setFactory;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge143.Triangle120PairFinder#findPairsOfSidesLessThanN(int)
	 */
	@Override
	public Map<Integer, Set<Integer>> findPairsOfSidesLessThanN(int n) {
		
		final Map<Integer, Set<Integer>> pairs = mapFactory.createMap();
		
		// Get values for j, can be root of n at most
		for(int j = 1, j2 = j * j; j2 < n; ++j, j2 = j * j) {
			// Get values for k, can be root of the remainder
			for(int k = 1, k2 = k * k; k2 <= j2; ++k, k2 = k * k) {
				final int a = 2 * j * k + k2;
				final int b = j2 - k2;
				
				final int shortest = Math.min(a, b);
				final int longest = Math.max(a, b);
				
				for(int multiplier = 1, sm = shortest * multiplier, lm = longest * multiplier;
						((sm + lm) <= n) && (sm > 0);
						++multiplier, sm = shortest * multiplier, lm = longest * multiplier) {
					Set<Integer> longer = pairs.get(sm);
					if(longer == null) {
						longer = setFactory.createSet();
						pairs.put(sm, longer);
					}
					longer.add(lm);
				}
			}
		}
		
		return pairs;
	}
	
	private final SetFactory setFactory;
	private final MapFactory mapFactory;

}
