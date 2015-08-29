/**
 * 
 */
package projectEuler.challenge010;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge010Caller implements Challenge {
	
	public Challenge010Caller(Challenge010 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		long result = challenge.findSumOfAllPrimesUpToN(2000000);
		String formatted = String.format("%d", result);
		return formatted;
	}
	
	private final Challenge010 challenge;

}
