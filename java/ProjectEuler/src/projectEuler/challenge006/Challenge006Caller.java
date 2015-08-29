/**
 * 
 */
package projectEuler.challenge006;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge006Caller implements Challenge {
	
	public Challenge006Caller(Challenge006 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		int result = challenge.findDifferenceBetweenSqSumAndSumSq(100);
		String formatted = String.format("%d", result);
		return formatted;
	}
	
	private final Challenge006 challenge;

}