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
public class BruteForceTriangle120PairFinder implements Triangle120PairFinder {
	
	public BruteForceTriangle120PairFinder(MapFactory mapFactory, SetFactory setFactory, Triangle120SideVerifier verifier) {
		this.mapFactory = mapFactory;
		this.setFactory = setFactory;
		this.verifier = verifier;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge143.Triangle120PairFinder#findPairsOfSidesLessThanN(int)
	 */
	@Override
	public Map<Integer, Set<Integer>> findPairsOfSidesLessThanN(int n) {
		
		Map<Integer, Set<Integer>> pairs = mapFactory.createMap();

		// Find triplets (a, b, c) where a <= b <= c
		final int aLimit = n / 3 + 1;
		for(int a = 1; a != aLimit; ++a) {
			final int nRemainingA = n - a;
			final int bLimit = nRemainingA + 1;
			for(int b = a; b != bLimit; ++b) {
				final boolean abOk = verifier.areShortSidesOf120DegTriangle(a, b);
				if(abOk) {
					final int shorter = Math.min(a, b);
					final int longer = Math.max(a, b);
					
					Set<Integer> longerSet = pairs.get(shorter);
					if(longerSet == null) {
						longerSet = setFactory.createSet();
						pairs.put(shorter, longerSet);
					}
					longerSet.add(longer);
				}
			}
		}
		
		return pairs;
	}
	
	private final MapFactory mapFactory;
	private final SetFactory setFactory;
	private final Triangle120SideVerifier verifier;

}
