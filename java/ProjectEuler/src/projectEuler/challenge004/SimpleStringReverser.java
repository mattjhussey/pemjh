/**
 * 
 */
package projectEuler.challenge004;

/**
 * @author matt
 *
 */
public final class SimpleStringReverser implements StringReverser {

	/* (non-Javadoc)
	 * @see projectEuler.challenge004.StringReverser#reverseString(java.lang.String)
	 */
	@Override
	public String reverseString(String forward) {
		char[] forwardChars = forward.toCharArray();
		StringBuilder sb = new StringBuilder();
		for(int index = forward.length() - 1; index != -1; --index) {
			char c = forwardChars[index];
			sb.append(c);
		}
		return sb.toString();
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
