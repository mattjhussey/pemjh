/**
 * 
 */
package projectEuler.challenge150;

/**
 * @author matt
 *
 */
public final class SimpleCoordinate implements Coordinate {
	public SimpleCoordinate(int row, int column) {
		this.row = row;
		this.column = column;
		hashCode = ((row + column) * (row + column) + row - column) / 2;
	}
	
	@Override
	public int hashCode() {
		return hashCode;
	}
	
	@Override
	public boolean equals(Object obj) {
		boolean correctType = obj instanceof SimpleCoordinate;
		if(!correctType) {
			return false;
		}
		
		SimpleCoordinate other = (SimpleCoordinate) obj;
		
		boolean isEqual = (other.row == this.row) && (other.column == this.column);
		
		return isEqual;
	}
	
	private final int row;
	private final int column;
	private final int hashCode;
}
