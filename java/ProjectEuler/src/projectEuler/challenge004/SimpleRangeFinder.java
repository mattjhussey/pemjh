/**
 * 
 */
package projectEuler.challenge004;

/**
 * @author matt
 *
 */
public final class SimpleRangeFinder implements RangeFinder {

	@Override
	public Range findRangeWithNDigits(int n) {
		int minimum = (int)Math.pow(10, n - 1);
		int maximum = (int)Math.pow(10, n);
		
		Range result = new SimpleRange(minimum, maximum);
		
		return result;
	}

}
