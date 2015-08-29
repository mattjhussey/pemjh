/**
 * 
 */
package projectEuler.challenge006.test;

import static org.junit.Assert.assertEquals;

import org.jmock.Expectations;
import org.jmock.integration.junit4.JUnitRuleMockery;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import projectEuler.challenge006.SimpleChallenge006;
import projectEuler.challenge006.SumFinder;
import projectEuler.challenge006.SumOfSquaresFinder;

/**
 * @author matt
 *
 */
public final class SimpleChallenge006Test {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final SumFinder sumFinder = context.mock(SumFinder.class);
	private final SumOfSquaresFinder sumOfSquaresFinder = context.mock(SumOfSquaresFinder.class);
	private final SimpleChallenge006 challenge = new SimpleChallenge006(sumFinder, sumOfSquaresFinder);

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
	 * Test method for {@link projectEuler.challenge006.SimpleChallenge006#findDifferenceBetweenSqSumAndSumSq(int)}.
	 */
	@Test
	public final void testFindDifferenceBetweenSqSumAndSumSq() {
		final int n = 10;
		final int sumToN = 55;
		final int squareSumToN = 385;
		
		context.checking(new Expectations() {
			{
				oneOf(sumFinder).findSumUpToN(with(equal(n))); will(returnValue(sumToN));
				oneOf(sumOfSquaresFinder).findSumOfSquaresUpToN(with(equal(n))); will(returnValue(squareSumToN));
			}
		});
		
		final int actual = challenge.findDifferenceBetweenSqSumAndSumSq(n);
		final int expected = 2640;
		assertEquals(expected, actual);
	}

}
