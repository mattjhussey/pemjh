/**
 * 
 */
package projectEuler.challenge004;

/**
 * @author matt
 *
 */
public interface RangeFinder {
	/**
	 * Return range of numbers containing n digits [min, max).
	 * eg. for 2 return 10 and 100; for 3 return 100 and 1000
	 * @param n
	 * @return
	 */
	Range findRangeWithNDigits(int n);
}
