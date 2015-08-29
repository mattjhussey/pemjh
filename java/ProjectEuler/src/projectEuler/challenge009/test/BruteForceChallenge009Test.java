/**
 * 
 */
package projectEuler.challenge009.test;

import static org.junit.Assert.assertEquals;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import projectEuler.challenge009.BruteForceChallenge009;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge009Test {
	private final BruteForceChallenge009 challenge = new BruteForceChallenge009();

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
	 * Test method for {@link projectEuler.challenge009.BruteForceChallenge009#findProductTripletWhereSumIsN(int)}.
	 */
	@Test
	public final void testFindProductTripletWhereSumIsN() {
		int actual = challenge.findProductTripletWhereSumIsN(12);
		int expected = 60;
		assertEquals(expected, actual);
	}

}
