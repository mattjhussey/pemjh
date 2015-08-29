/**
 * 
 */
package projectEuler.challenge147.test;

import static org.junit.Assert.*;

import org.jmock.Expectations;
import org.jmock.integration.junit4.JUnitRuleMockery;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import projectEuler.challenge147.AlignedRectangleFinder;
import projectEuler.challenge147.BruteForceChallenge147;
import projectEuler.challenge147.DiagonalRectangleFinder;

/**
 * @author matt
 *
 */
public class BruteForceChallenge147Test {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final AlignedRectangleFinder alignedRectangleFinder = context.mock(AlignedRectangleFinder.class);
	private final DiagonalRectangleFinder diagonalRectangleFinder = context.mock(DiagonalRectangleFinder.class);
	private final BruteForceChallenge147 challenge = new BruteForceChallenge147(alignedRectangleFinder, diagonalRectangleFinder);

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
	 * Test method for {@link projectEuler.challenge147.BruteForceChallenge147#findTotalRectanglesInGridsMNAndSmaller(int, int)}.
	 */
	@Test
	public final void testFindTotalRectanglesInGridsMNAndSmaller() {
		final int m = 3;
		final int n = 2;
		
		final int a1_1 = 1;
		final int a1_2 = 3;
		final int a2_1 = 3;
		final int a2_2 = 9;
		final int a3_1 = 6;
		final int a3_2 = 18;
		
		final int d1_1 = 0;
		final int d1_2 = 1;
		final int d2_1 = 1;
		final int d2_2 = 9;
		final int d3_1 = 2;
		final int d3_2 = 19;
		
		context.checking(new Expectations() {
			{
				oneOf(alignedRectangleFinder).findNumberOfRectanglesInMN(with(equal(1)), with(equal(1))); will(returnValue(a1_1));
				oneOf(alignedRectangleFinder).findNumberOfRectanglesInMN(with(equal(1)), with(equal(2))); will(returnValue(a1_2));
				oneOf(alignedRectangleFinder).findNumberOfRectanglesInMN(with(equal(2)), with(equal(1))); will(returnValue(a2_1));
				oneOf(alignedRectangleFinder).findNumberOfRectanglesInMN(with(equal(2)), with(equal(2))); will(returnValue(a2_2));
				oneOf(alignedRectangleFinder).findNumberOfRectanglesInMN(with(equal(3)), with(equal(1))); will(returnValue(a3_1));
				oneOf(alignedRectangleFinder).findNumberOfRectanglesInMN(with(equal(3)), with(equal(2))); will(returnValue(a3_2));
				
				oneOf(diagonalRectangleFinder).findNumberOfRectanglesInMN(with(equal(1)), with(equal(1))); will(returnValue(d1_1));
				oneOf(diagonalRectangleFinder).findNumberOfRectanglesInMN(with(equal(1)), with(equal(2))); will(returnValue(d1_2));
				oneOf(diagonalRectangleFinder).findNumberOfRectanglesInMN(with(equal(2)), with(equal(1))); will(returnValue(d2_1));
				oneOf(diagonalRectangleFinder).findNumberOfRectanglesInMN(with(equal(2)), with(equal(2))); will(returnValue(d2_2));
				oneOf(diagonalRectangleFinder).findNumberOfRectanglesInMN(with(equal(3)), with(equal(1))); will(returnValue(d3_1));
				oneOf(diagonalRectangleFinder).findNumberOfRectanglesInMN(with(equal(3)), with(equal(2))); will(returnValue(d3_2));
			}
		});
		
		final long actual = challenge.findTotalRectanglesInGridsMNAndSmaller(m, n);
		final long expected = 72;
		assertEquals(expected, actual);
	}

}
