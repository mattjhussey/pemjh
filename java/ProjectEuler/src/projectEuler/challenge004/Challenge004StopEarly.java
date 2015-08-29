/**
 * 
 */
package projectEuler.challenge004;

/**
 * @author matt
 *
 */
public final class Challenge004StopEarly implements Challenge004 {
	
	public Challenge004StopEarly(PalindromeValidator palindromeValidator, RangeFinder rangeFinder) {
		this.palindromeValidator = palindromeValidator;
		this.rangeFinder = rangeFinder;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge004.Challenge004#getLargestPalindromeOfDigitProduct(int)
	 */
	@Override
	public int getLargestPalindromeOfDigitProduct(int numDigitsInFactor) {
		Range range = rangeFinder.findRangeWithNDigits(numDigitsInFactor);
		
		int maximum = range.getMaximum() - 1;
		int minimum = range.getMinimum() - 1;
		
		int largestPalindrome = Integer.MIN_VALUE;
		
		for(int a = maximum; a != minimum; --a) {
			int largestProduct = a * a;
			if(largestProduct < largestPalindrome) {
				// Answer found
				break;
			} else {
				for(int b = a; b != minimum; --b) {
					int product = a * b;
					
					if(product < largestPalindrome) {
						// Best answer for a found
						break;
					} else {					
						boolean isPalindrome = palindromeValidator.isPalindrome(product);
						
						if(isPalindrome) { 
							if(product > largestPalindrome) {
								largestPalindrome = product;
							}
						}
					}
				}
			}
		}
		
		return largestPalindrome;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	private final PalindromeValidator palindromeValidator;
	private final RangeFinder rangeFinder;

}
