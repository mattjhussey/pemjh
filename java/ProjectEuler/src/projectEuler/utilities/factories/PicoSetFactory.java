/**
 * 
 */
package projectEuler.utilities.factories;

import java.util.Set;

import org.picocontainer.PicoContainer;


/**
 * @author matt
 *
 */
public class PicoSetFactory implements SetFactory {
	
	public PicoSetFactory(PicoContainer picoContainer) {
		this.picoContainer = picoContainer;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge141.SetFactory#createSet()
	 */
	@SuppressWarnings("unchecked")
	@Override
	public <T> Set<T> createSet() {
		return picoContainer.getComponent(Set.class);
	}
	
	private final PicoContainer picoContainer;

}
