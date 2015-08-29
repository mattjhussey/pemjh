/**
 * 
 */
package projectEuler.challenge150;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public class Challenge150Caller implements Challenge {
	
	public Challenge150Caller(Challenge150 challenge, Triangle triangle) {
		this.challenge = challenge;
		this.triangle = triangle;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {		
		long result = challenge.findSmallestTriangleSum(triangle);
		String formatted = String.format("%d", result);
		return formatted;
	}
	
	private final Challenge150 challenge;
	private final Triangle triangle;

}
