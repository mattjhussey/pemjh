/**
 * 
 */
package projectEuler.challenge004;

/**
 * @author matt
 *
 */
public final class StringReversingPalindromeValidator implements PalindromeValidator {
	
	public StringReversingPalindromeValidator(StringReverser stringReverser) {
		this.stringReverser = stringReverser;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge004.PalindromeValidator#isPalindrome(int)
	 */
	@Override
	public boolean isPalindrome(int number) {
		if(number < 10) {
			// Single numbers cannot be palindromic
			return false;
		}
		String forward = String.format("%d", number);
		String backward = stringReverser.reverseString(forward);
		return forward.equals(backward);
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	private final StringReverser stringReverser;

}
