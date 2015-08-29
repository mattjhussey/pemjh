/**
 * 
 */
package projectEuler.challenge004.test;

import static org.junit.Assert.assertTrue;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import projectEuler.challenge004.Range;
import projectEuler.challenge004.SimpleRange;
import projectEuler.challenge004.SimpleRangeComparator;
import projectEuler.challenge004.SimpleRangeFinder;

/**
 * @author matt
 *
 */
public final class SimpleRangeFinderTest {
	private final SimpleRangeFinder rangeFinder = new SimpleRangeFinder();

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
	 * Test method for {@link projectEuler.challenge004.SimpleRangeFinder#findRangeWithNDigits(int)}.
	 */
	@Test
	public final void testFindRangeWithNDigits() {
		final Range with1DigitActual = rangeFinder.findRangeWithNDigits(2);
		final Range with1DigitExpected = new SimpleRange(10, 100);
		SimpleRangeComparator comparator = new SimpleRangeComparator();
		assertTrue(comparator.compare(with1DigitExpected, with1DigitActual) == 0);
	}

}
