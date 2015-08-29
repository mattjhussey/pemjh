/**
 * 
 */
package projectEuler.challenge140;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge140Caller implements Challenge {
	
	public Challenge140Caller(Challenge140 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		long result = challenge.findSumOfFirstNNuggets(30);
		String formatted = String.format("%d", result);
		return formatted;
	}
	
	private final Challenge140 challenge;

}
