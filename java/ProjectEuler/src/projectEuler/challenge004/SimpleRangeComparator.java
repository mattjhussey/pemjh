/**
 * 
 */
package projectEuler.challenge004;

/**
 * @author matt
 *
 */
public final class SimpleRangeComparator implements RangeComparator {

	/* (non-Javadoc)
	 * @see java.util.Comparator#compare(java.lang.Object, java.lang.Object)
	 */
	@Override
	public int compare(Range arg0, Range arg1) {
		// Greater max is "higher", then Greater min is "higher"
		final int EQUAL = 0;
		
		// Save on potentially slow calls by getting now
		int arg0Max = arg0.getMaximum();
		int arg1Max = arg1.getMaximum();
		
		int maxComparison = Integer.compare(arg0Max, arg1Max);
		
		if(maxComparison == EQUAL) {
			int arg0Min = arg0.getMinimum();
			int arg1Min = arg1.getMinimum();
			
			int minComparison = Integer.compare(arg0Min, arg1Min);
			
			return minComparison;
		}
		
		return maxComparison;
	}

}
