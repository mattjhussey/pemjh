/**
 * 
 */
package projectEuler.challenge147;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public class Challenge147Caller implements Challenge {
	
	public Challenge147Caller(Challenge147 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		long result = challenge.findTotalRectanglesInGridsMNAndSmaller(47, 43);
		String formatted = String.format("%d", result);
		return formatted;
	}
	
	private final Challenge147 challenge;

}
