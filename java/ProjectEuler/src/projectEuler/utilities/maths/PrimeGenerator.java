/**
 * 
 */
package projectEuler.utilities.maths;

import java.util.SortedSet;

/**
 * @author matt
 *
 */
public interface PrimeGenerator {
	/**
	 * Return an List of prime numbers up to and including n
	 */
	SortedSet<Integer> findPrimesUpToN(int n);
}
