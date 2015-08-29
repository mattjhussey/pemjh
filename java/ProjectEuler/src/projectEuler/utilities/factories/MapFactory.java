/**
 * 
 */
package projectEuler.utilities.factories;

import java.util.Map;

/**
 * @author matt
 *
 */
public interface MapFactory {
	<K, V> Map<K, V> createMap();
}
