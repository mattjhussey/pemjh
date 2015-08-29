/**
 * 
 */
package projectEuler.challenge007;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge007Caller implements Challenge {
	
	public Challenge007Caller(Challenge007 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		int result = challenge.findNthPrime(10_001);
		String formatted = String.format("%d", result);
		return formatted;
	}
	
	private final Challenge007 challenge;

}
