/**
 * 
 */
package projectEuler.challenge147;

/**
 * @author matt
 *
 */
public class BruteForceDiagonalRectangleFinder implements
		DiagonalRectangleFinder {

	/* (non-Javadoc)
	 * @see projectEuler.challenge147.DiagonalRectangleFinder#findNumberOfRectanglesInMN(int, int)
	 */
	@Override
	public int findNumberOfRectanglesInMN(int m, int n) {
		
		final int shortest = Math.min(m, n);
		final int longest = Math.max(m, n);
		
		// Equation worked out from playing in loCalc and seems to work
		// Replaced equation with one from pe forum since it's neater
		final int answer = ((longest + longest - shortest) * (shortest * shortest * 4 - 1) - 3) * shortest / 6;
		
		return answer;
	}

}
