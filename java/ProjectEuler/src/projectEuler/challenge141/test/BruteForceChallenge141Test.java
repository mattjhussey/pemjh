/**
 * 
 */
package projectEuler.challenge141.test;

import static org.junit.Assert.assertEquals;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Ignore;
import org.junit.Test;

import projectEuler.challenge141.BruteForceChallenge141;

/**
 * @author matt
 *
 */
@Ignore("Very slow tests and superceded by the CutDownChallenge141 implementation")
public final class BruteForceChallenge141Test {
	private final BruteForceChallenge141 challenge = new BruteForceChallenge141();

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
	 * Test method for {@link projectEuler.challenge141.BruteForceChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN() {
		final long n = 10;
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final int expected = 9;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.BruteForceChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_100000() {
		final long n = 100000;		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final int expected = 124657;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.BruteForceChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_1000000() {
		final long n = 1000000;		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final int expected = 700738;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.BruteForceChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_10000000() {
		final long n = 10000000;		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final int expected = 14253190;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.BruteForceChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_100000000() {
		final long n = 100000000;		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final int expected = 171436696;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.BruteForceChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_1000000000() {
		final long n = 1000000000;		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final int expected = 623708737;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.BruteForceChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_10000000000() {
		final long n = 10_000_000_000l;		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 21630503507l;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.BruteForceChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_100000000000() {
		final long n = 100_000_000_000l;		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 64431087395l;
		assertEquals(expected, actual);
	}

}
