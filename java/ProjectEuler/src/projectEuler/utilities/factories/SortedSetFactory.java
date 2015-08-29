/**
 * 
 */
package projectEuler.utilities.factories;

import java.util.SortedSet;

/**
 * @author matt
 *
 */
public interface SortedSetFactory {
	<T> SortedSet<T> createSortedSet();
}
