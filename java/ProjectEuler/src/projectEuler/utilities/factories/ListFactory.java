/**
 * 
 */
package projectEuler.utilities.factories;

import java.util.List;

/**
 * @author matt
 *
 */
public interface ListFactory {
	<T> List<T> createList();
}
