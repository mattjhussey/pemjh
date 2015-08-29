/**
 * 
 */
package projectEuler.utilities.factories;

import java.util.Set;

/**
 * @author matt
 *
 */
public interface SetFactory {
	<T> Set<T> createSet();
}
