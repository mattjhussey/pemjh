/**
 * 
 */
package projectEuler.challenge006.test;

import static org.junit.Assert.assertEquals;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import projectEuler.challenge006.ClosedFunctionSumOfSquaresFinder;

/**
 * @author matt
 *
 */
public final class ClosedFunctionSumOfSquaresFinderTest {
	private final ClosedFunctionSumOfSquaresFinder sumOfSquaresFinder = new ClosedFunctionSumOfSquaresFinder();

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
	 * Test method for {@link projectEuler.challenge006.ClosedFunctionSumOfSquaresFinder#findSumOfSquaresUpToN(int)}.
	 */
	@Test
	public final void testFindSumOfSquaresUpToN() {
		final int n = 10;
		final int actual = sumOfSquaresFinder.findSumOfSquaresUpToN(n);
		final int expected = 385;
		assertEquals(expected, actual);
	}

}
