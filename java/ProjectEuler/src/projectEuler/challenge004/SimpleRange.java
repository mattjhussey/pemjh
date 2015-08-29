/**
 * 
 */
package projectEuler.challenge004;

/**
 * @author matt
 *
 */
public final class SimpleRange implements Range {
	
	public SimpleRange(int minimum, int maximum) {
		this.minimum = minimum;
		this.maximum = maximum;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge004.Range#minimum()
	 */
	@Override
	public int getMinimum() {
		return minimum;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge004.Range#maximum()
	 */
	@Override
	public int getMaximum() {
		return maximum;
	}
	
	private final int minimum;
	private final int maximum;

}
