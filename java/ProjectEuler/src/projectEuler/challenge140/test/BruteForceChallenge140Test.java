/**
 * 
 */
package projectEuler.challenge140.test;

import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.List;

import org.jmock.Expectations;
import org.jmock.integration.junit4.JUnitRuleMockery;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import projectEuler.challenge140.BruteForceChallenge140;
import projectEuler.challenge140.GoldenNuggetGenerator;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge140Test {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final GoldenNuggetGenerator generator = context.mock(GoldenNuggetGenerator.class);
	private final BruteForceChallenge140 challenge = new BruteForceChallenge140(generator);

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
	 * Test method for {@link projectEuler.challenge140.BruteForceChallenge140#findSumOfFirstNNuggets(int)}.
	 */
	@Test
	public final void testFindSumOfFirstNNuggets() {
		final int n = 5;
		
		final List<Long> nuggets = new ArrayList<>();
		nuggets.add(1l);
		nuggets.add(2l);
		nuggets.add(3l);
		nuggets.add(4l);
		nuggets.add(5l);
		
		context.checking(new Expectations() {
			{
				oneOf(generator).generateNGoldenNuggets(with(equal(n))); will(returnValue(nuggets));
			}
		});
		
		final long actual = challenge.findSumOfFirstNNuggets(n);
		final int expected = 15;
		assertEquals(expected, actual);
	}

}
