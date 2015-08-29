/**
 * 
 */
package projectEuler.challenge143;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge143Caller implements Challenge {
	
	public Challenge143Caller(Challenge143 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		long result = challenge.findFermatPointSumsUpToN(120_000);
		String formatted = String.format("%d", result);
		return formatted;
	}
	
	private final Challenge143 challenge;

}
