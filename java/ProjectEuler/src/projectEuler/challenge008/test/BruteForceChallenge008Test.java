/**
 * 
 */
package projectEuler.challenge008.test;

import static org.junit.Assert.assertEquals;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import projectEuler.challenge008.BruteForceChallenge008;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge008Test {
	private final BruteForceChallenge008 challenge = new BruteForceChallenge008();

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
	 * Test method for {@link projectEuler.challenge008.BruteForceChallenge008#findHighest5DigitProduct(java.lang.String)}.
	 */
	@Test
	public final void testFindHighest5DigitProduct() {
		final int actual = challenge.findHighest5DigitProduct("12345678900000987654321");
		final int expected = 15120;
		assertEquals(expected, actual);
	}

}
