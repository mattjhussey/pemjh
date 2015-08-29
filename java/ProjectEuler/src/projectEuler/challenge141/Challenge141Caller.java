/**
 * 
 */
package projectEuler.challenge141;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge141Caller implements Challenge {
	
	public Challenge141Caller(Challenge141 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		long result = challenge.findSumOfProgressiveSquaresBelowN(1000000000000l);
		String formatted = String.format("%d", result);
		return formatted;
	}
	
	private final Challenge141 challenge;

}
