/**
 * 
 */
package projectEuler.challenge143;

import java.util.Map;
import java.util.Set;

/**
 * @author matt
 *
 */
public interface Triangle120PairFinder {
	/**
	 * Find pairs of sides that make up a triangle with 120degrees between the two sides.
	 * The longest side is not needed.
	 * The shortest side shall be the key and any suitable long sides will be in the paired set
	 * The sum of each short and long side will not exceed n
	 * @param n
	 * @return
	 */
	Map<Integer, Set<Integer>> findPairsOfSidesLessThanN(int n);
}
