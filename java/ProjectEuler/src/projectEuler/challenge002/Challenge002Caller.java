/**
 * 
 */
package projectEuler.challenge002;

import projectEuler.Challenge;

/**
 * @author matt
 *
 */
public final class Challenge002Caller implements Challenge {
	
	public Challenge002Caller(Challenge002 challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		int result = challenge.getFibonacciSum(4000000);
		String formatted = String.format("%s", result);
		return formatted;
	}

	/**
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {
		System.out.println(new Challenge002Caller(new Challenge002BruteForce()).call());
	}
	
	private final Challenge002 challenge;

}
