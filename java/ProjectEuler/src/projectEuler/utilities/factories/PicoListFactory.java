/**
 * 
 */
package projectEuler.utilities.factories;

import java.util.List;

import org.picocontainer.PicoContainer;


/**
 * @author matt
 *
 */
public final class PicoListFactory implements ListFactory {
	
	public PicoListFactory(PicoContainer picoContainer) {
		this.picoContainer = picoContainer;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge005.ListFactory#createList()
	 */
	@SuppressWarnings("unchecked")
	@Override
	public <T> List<T> createList() {
		return picoContainer.getComponent(List.class);
	}
	
	private final PicoContainer picoContainer;

}
