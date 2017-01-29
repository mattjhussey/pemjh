/**
 * 
 */
package projectEuler.challenge150;


/**
 * @author matt
 *
 */
public class SimpleCoordinateFactory implements CoordinateFactory {

	/* (non-Javadoc)
	 * @see projectEuler.challenge150.CoordinateFactory#createCoordinate(int, int)
	 */
	@Override
	public Coordinate createCoordinate(int row, int column) {
		return new SimpleCoordinate(row, column);
	}

}
