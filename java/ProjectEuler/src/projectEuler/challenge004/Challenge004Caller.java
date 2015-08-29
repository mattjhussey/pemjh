/**
 * 
 */
package projectEuler.challenge004;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge004Caller implements Challenge {
	
	public Challenge004Caller(Challenge004 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		int result = challenge.getLargestPalindromeOfDigitProduct(3);
		String formatted = String.format("%d", result);
		return formatted;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	private final Challenge004 challenge;

}
