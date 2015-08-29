/**
 * 
 */
package projectEuler.challenge003;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge003Caller implements Challenge {
	
	public Challenge003Caller(Challenge003 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		long result = challenge.getLargestPrimeFactor(600851475143L);
		String formatted = String.format("%d", result);
		return formatted;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	private final Challenge003 challenge;

}
