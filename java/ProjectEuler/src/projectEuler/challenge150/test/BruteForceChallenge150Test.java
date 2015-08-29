/**
 * 
 */
package projectEuler.challenge150.test;

import static org.junit.Assert.assertEquals;

import java.util.HashMap;
import java.util.Map;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import projectEuler.challenge150.BruteForceChallenge150;
import projectEuler.challenge150.Coordinate;
import projectEuler.challenge150.CoordinateFactory;
import projectEuler.challenge150.SimpleCoordinate;
import projectEuler.challenge150.TestTriangle;
import projectEuler.challenge150.Triangle;
import projectEuler.utilities.factories.MapFactory;

/**
 * @author matt
 *
 */
public class BruteForceChallenge150Test {
	private final BruteForceChallenge150 challenge = new BruteForceChallenge150();

	/**
	 * @throws java.lang.Exception
	 */
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
	}

	/**
	 * @throws java.lang.Exception
	 */
	@AfterClass
	public static void tearDownAfterClass() throws Exception {
	}

	/**
	 * @throws java.lang.Exception
	 */
	@Before
	public void setUp() throws Exception {
	}

	/**
	 * @throws java.lang.Exception
	 */
	@After
	public void tearDown() throws Exception {
	}

	/**
	 * Test method for {@link projectEuler.challenge150.BruteForceChallenge150#findSmallestTriangleSum(java.util.List)}.
	 */
	@Test
	public final void testFindSmallestTriangleSum() {
		MapFactory mapFactory = new MapFactory() {
			
			@Override
			public <K, V> Map<K, V> createMap() {
				return new HashMap<>();
			}
		};
		
		CoordinateFactory coordinateFactory = new CoordinateFactory() {
			
			@Override
			public Coordinate createCoordinate(int row, int column) {
				return new SimpleCoordinate(row, column);
			}
		};
		
		Triangle triangle = new TestTriangle(mapFactory, coordinateFactory);
		
		final long actual = challenge.findSmallestTriangleSum(triangle);
		final long expected = -42;
		assertEquals(expected, actual);
	}

}
