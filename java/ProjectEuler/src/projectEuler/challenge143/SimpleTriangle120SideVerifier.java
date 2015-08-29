/**
 * 
 */
package projectEuler.challenge143;

/**
 * @author matt
 *
 */
public class SimpleTriangle120SideVerifier implements Triangle120SideVerifier {

	/* (non-Javadoc)
	 * @see projectEuler.challenge143.Triangle120SideVerifier#areShortSidesOf120DegTriangle(int, int)
	 */
	@Override
	public boolean areShortSidesOf120DegTriangle(int a, int b) {
		final long al = (long) a;
		final long bl = (long) b;
		final long result = al * al + al * bl + bl * bl;
		final long root = (long) Math.sqrt(result);
		final long rebuilt = root * root;
		return rebuilt == result;
	}

}
