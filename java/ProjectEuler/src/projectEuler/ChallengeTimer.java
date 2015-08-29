/**
 * 
 */
package projectEuler;

/**
 * @author matt
 *
 */
public final class ChallengeTimer implements Challenge {
	
	private final Challenge challenge;
	
	public ChallengeTimer(Challenge challenge) {
		this.challenge = challenge;
	}

	/* (non-Javadoc)
	 * @see java.util.concurrent.Callable#call()
	 */
	@Override
	public String call() throws Exception {
		long start = System.currentTimeMillis();
		String result = challenge.call();
		long end = System.currentTimeMillis();
		long time = end - start;
		String formattedResult = String.format("%s (%d milliseconds)", result, time);
		return formattedResult;
	}

}
