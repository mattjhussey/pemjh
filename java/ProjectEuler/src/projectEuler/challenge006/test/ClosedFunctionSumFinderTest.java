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

import projectEuler.challenge006.ClosedFunctionSumFinder;

/**
 * @author matt
 *
 */
public final class ClosedFunctionSumFinderTest {
	private final ClosedFunctionSumFinder sumFinder = new ClosedFunctionSumFinder();

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
	 * Test method for {@link projectEuler.challenge006.ClosedFunctionSumFinder#findSumUpToN(int)}.
	 */
	@Test
	public final void testFindSumUpToN() {
		final int n = 10;
		final int actual = sumFinder.findSumUpToN(n);
		final int expected = 55;
		assertEquals(expected, actual);
	}

}
