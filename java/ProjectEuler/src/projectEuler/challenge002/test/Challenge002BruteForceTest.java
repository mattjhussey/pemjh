/**
 * 
 */
package projectEuler.challenge002.test;

import static org.junit.Assert.assertEquals;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import projectEuler.challenge002.Challenge002BruteForce;

/**
 * @author matt
 *
 */
public final class Challenge002BruteForceTest {
	
	private final Challenge002BruteForce challenge = new Challenge002BruteForce();

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
	 * Test method for {@link projectEuler.challenge002.Challenge002BruteForce#getFibonacciSum(int)}.
	 */
	@Test
	public final void testGetFibonacciSum() {
		final int actual = challenge.getFibonacciSum(90);
		final int expected = 44;
		
		assertEquals(expected, actual);
	}

}
