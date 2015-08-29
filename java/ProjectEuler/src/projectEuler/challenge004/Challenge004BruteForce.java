/**
 * 
 */
package projectEuler.challenge004;

/**
 * @author matt
 *
 */
public final class Challenge004BruteForce implements Challenge004 {
	
	public Challenge004BruteForce(PalindromeValidator palindromeValidator, RangeFinder rangeFinder) {
		this.palindromeValidator = palindromeValidator;
		this.rangeFinder = rangeFinder;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge004.Challenge004#getLargestPalindromeOfDigitProduct(int)
	 */
	@Override
	public int getLargestPalindromeOfDigitProduct(int numDigitsInFactor) {
		// Get range of digits
		Range range = rangeFinder.findRangeWithNDigits(numDigitsInFactor);
		
		int largestPalindrome = Integer.MIN_VALUE;
		
		int maximum = range.getMaximum() - 1;
		int minimum = range.getMinimum() - 1;
		
		for(int a = maximum; a != minimum; --a) {
			for(int b = a; b != minimum; --b) {
				int product = a * b;
				
				boolean isPalindrome = palindromeValidator.isPalindrome(product);
				
				if(isPalindrome) { 
					if(product > largestPalindrome) {
						largestPalindrome = product;
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
