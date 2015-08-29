/**
 * 
 */
package projectEuler.challenge005.test;

import static org.junit.Assert.assertEquals;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import projectEuler.challenge005.BruteForceChallenge005;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge005Test {
	private final BruteForceChallenge005 challenge = new BruteForceChallenge005();

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
	 * Test method for {@link projectEuler.challenge005.BruteForceChallenge005#findLowestCommonDenominatorOfNumsUpToN(int)}.
	 */
	@Test
	public final void testFindLowestCommonDenominatorOfNumsUpToN() {
		int lcd = challenge.findLowestCommonDenominatorOfNumsUpToN(10);
		int expected = 2520;
		assertEquals(expected, lcd);
	}

}
