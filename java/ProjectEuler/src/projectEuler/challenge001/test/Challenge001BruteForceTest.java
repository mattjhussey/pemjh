/**
 * 
 */
package projectEuler.challenge001.test;

import static org.junit.Assert.assertEquals;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import projectEuler.challenge001.Challenge001BruteForce;

/**
 * @author matt
 *
 */
public final class Challenge001BruteForceTest {
	private final Challenge001BruteForce challenge001 = new Challenge001BruteForce();

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
	 * Test method for {@link projectEuler.challenge001.Challenge001BruteForce#getSumOf3And5Multiples(int)}.
	 */
	@Test
	public final void testGetSumOf3And5MultiplesSimpleCase() {
		final int result = challenge001.getSumOf3And5Multiples(10);
		final int expected = 23;
		
		assertEquals(expected, result);
	}

}
