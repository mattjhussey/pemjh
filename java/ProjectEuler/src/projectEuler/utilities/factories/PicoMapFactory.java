/**
 * 
 */
package projectEuler.utilities.factories;

import java.util.Map;

import org.picocontainer.PicoContainer;


/**
 * @author matt
 *
 */
public final class PicoMapFactory implements MapFactory {
	
	public PicoMapFactory(PicoContainer picocontainer) {
		this.picocontainer = picocontainer;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge005.MapFactory#getMap()
	 */
	@SuppressWarnings("unchecked")
	@Override
	public <K, V> Map<K, V> createMap() {
		return picocontainer.getComponent(Map.class);
	}
	
	private final PicoContainer picocontainer;

}
