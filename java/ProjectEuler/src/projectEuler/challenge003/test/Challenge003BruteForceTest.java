/**
 * 
 */
package projectEuler.challenge003.test;

import static org.junit.Assert.assertEquals;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import projectEuler.challenge003.Challenge003BruteForce;

/**
 * @author matt
 *
 */
public final class Challenge003BruteForceTest {

	private final Challenge003BruteForce challenge = new Challenge003BruteForce();
	
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
	 * Test method for {@link projectEuler.challenge003.Challenge003BruteForce#getLargestPrimeFactor(int)}.
	 */
	@Test
	public final void testGetLargestPrimeFactor() {
		long actual = challenge.getLargestPrimeFactor(13195);
		long expected = 29;
		assertEquals(expected, actual);
	}

}
