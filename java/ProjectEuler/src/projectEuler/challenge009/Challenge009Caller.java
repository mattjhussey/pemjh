/**
 * 
 */
package projectEuler.challenge009;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge009Caller implements Challenge {
	
	public Challenge009Caller(Challenge009 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		int result = challenge.findProductTripletWhereSumIsN(1000);
		String formatted = String.format("%d", result);
		return formatted;
	}
	
	private final Challenge009 challenge;

}
