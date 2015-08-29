/**
 * 
 */
package projectEuler;

/**
 * @author matt
 *
 */
public final class ChallengeLabeller implements Challenge {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public ChallengeLabeller(Challenge wrapped, String label) {
		this.wrapped = wrapped;
		this.label = label;
	}

	@Override
	public String call() throws Exception {
		String result = wrapped.call();
		String labelled = String.format("%s: %s", label, result);
		return labelled;
	}
	
	private final Challenge wrapped;
	private final String label;

}
