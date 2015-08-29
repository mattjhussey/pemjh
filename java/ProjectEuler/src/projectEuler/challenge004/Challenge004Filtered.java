/**
 * 
 */
package projectEuler.challenge004;

/**
 * @author matt
 *
 */
public final class Challenge004Filtered implements Challenge004 {
	
	public Challenge004Filtered(PalindromeValidator palindromeValidator, RangeFinder rangeFinder) {
		this.palindromeValidator = palindromeValidator;
		this.rangeFinder = rangeFinder;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge004.Challenge004#getLargestPalindromeOfDigitProduct(int)
	 */
	@Override
	public int getLargestPalindromeOfDigitProduct(int numDigitsInFactor) {
		final Range range = rangeFinder.findRangeWithNDigits(numDigitsInFactor);
		
		final int maximum = range.getMaximum() - 1;
		
		// Palindromic numbers are always divisible by 11 so find highest number below maximum that is divisible by 11
		final int offset = maximum % 11;
		final int elevenMaximum = maximum - offset;
		
		final int minimum = range.getMinimum() - 1;
		
		int highestFound = Integer.MIN_VALUE;
		
		for(int elevens = elevenMaximum; elevens > minimum; elevens -= 11) {
			final int maximumProduct = elevens * maximum;
			if(maximumProduct < highestFound) {
				// Cannot better the found answer
				break;
			}
			
			for(int other = maximum; other != minimum; --other) {
				final int product = elevens * other;
				
				if(product > highestFound) {
					if(palindromeValidator.isPalindrome(product)) {
						highestFound = product;
						break;
					}
				} else {
					break;
				}
			}
		}
		
		return highestFound;
	}
	
	private final RangeFinder rangeFinder;
	private final PalindromeValidator palindromeValidator;

}
