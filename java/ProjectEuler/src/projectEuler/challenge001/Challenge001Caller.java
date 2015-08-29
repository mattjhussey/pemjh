/**
 * 
 */
package projectEuler.challenge001;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge001Caller implements Challenge {

	public Challenge001Caller(Challenge001 challenge) {
		this.challenge = challenge;
	}

	@Override
	public String call() throws Exception {
		int result = challenge.getSumOf3And5Multiples(1000);
		String formatted = String.format("%d", result);
		return formatted;
	}
	
	private final Challenge001 challenge;

}
