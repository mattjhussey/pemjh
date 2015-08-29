/**
 * 
 */
package projectEuler.utilities.factories;

import java.util.SortedSet;

import org.picocontainer.PicoContainer;


/**
 * @author matt
 *
 */
public final class PicoSortedSetFactory implements SortedSetFactory {
	
	public PicoSortedSetFactory(PicoContainer picoContainer) {
		this.picoContainer = picoContainer;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge005.SortedSetFactory#createSortedSet()
	 */
	@SuppressWarnings("unchecked")
	@Override
	public <T> SortedSet<T> createSortedSet() {
		return picoContainer.getComponent(SortedSet.class);
	}
	
	private final PicoContainer picoContainer;

}
