/**
 * 
 */
package projectEuler.challenge143.test;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import projectEuler.challenge143.SimpleTriangle120SideVerifier;

/**
 * @author matt
 *
 */
public class SimpleTriangle120SideVerifierTest {
	private final SimpleTriangle120SideVerifier verifier = new SimpleTriangle120SideVerifier();

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
	 * Test method for {@link projectEuler.challenge143.SimpleTriangle120SideVerifier#areShortSidesOf120DegTriangle(int, int)}.
	 */
	@Test
	public final void testAreShortSidesOf120DegTriangle_Valid() {
		final boolean actual = verifier.areShortSidesOf120DegTriangle(3, 5);
		// 3 and 5 are valid. When they are 120 degrees apart, the long side is: 7
		
		assertTrue(actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge143.SimpleTriangle120SideVerifier#areShortSidesOf120DegTriangle(int, int)}.
	 */
	@Test
	public final void testAreShortSidesOf120DegTriangle_Invalid() {
		final boolean actual = verifier.areShortSidesOf120DegTriangle(3, 4);
		// 3 and 4 are valid. When they are 120 degrees apart, the long side is: sqrt(37), so not integral
		
		assertFalse(actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge143.SimpleTriangle120SideVerifier#areShortSidesOf120DegTriangle(int, int)}.
	 */
	@Test
	public final void testAreShortSidesOf120DegTriangle_IntOverflow() {
		final int multiple = 143165576;
		final int m3 = multiple * 3;
		final int m5 = multiple * 5;
		// Using a multiplied up version of the 3,5,7 triangle
		final boolean actual = verifier.areShortSidesOf120DegTriangle(m3, m5);
		
		assertTrue(actual);
	}

}
