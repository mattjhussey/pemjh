/**
 * 
 */
package projectEuler.challenge005;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge005Caller implements Challenge {
	
	public Challenge005Caller(Challenge005 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		int result = challenge.findLowestCommonDenominatorOfNumsUpToN(20);
		String formatted = String.format("%d", result);
		return formatted;
	}
	
	private final Challenge005 challenge;

}
