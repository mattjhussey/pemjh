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

import projectEuler.challenge140.BruteForceGoldenNuggetGenerator;
import projectEuler.challenge140.FibonacciGenerator;
import projectEuler.utilities.factories.ListFactory;

/**
 * @author matt
 *
 */
public final class BruteForceGoldenNuggetGeneratorTest {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final ListFactory listFactory = context.mock(ListFactory.class);
	private final FibonacciGenerator fibonacciGenerator = context.mock(FibonacciGenerator.class);
	private final BruteForceGoldenNuggetGenerator goldenNuggetGenerator = new BruteForceGoldenNuggetGenerator(listFactory, fibonacciGenerator);

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
	 * Test method for {@link projectEuler.challenge140.BruteForceGoldenNuggetGenerator#generateNGoldenNuggets(int)}.
	 */
	@Test
	public final void testGenerateNGoldenNuggets() {
		final int n = 5;
		final int fibsNeeded = 2 * n - 1;
		final List<Long> list = new ArrayList<>();
		final List<Long> fibs = new ArrayList<>();
		fibs.add(1l);
		fibs.add(2l);
		fibs.add(3l);
		fibs.add(5l);
		fibs.add(8l);
		fibs.add(13l);
		fibs.add(21l);
		fibs.add(34l);
		fibs.add(55l);
		
		context.checking(new Expectations() {
			{
				oneOf(listFactory).createList(); will(returnValue(list));
				oneOf(fibonacciGenerator).generateNFibonacciNumbers(with(equal(fibsNeeded))); will(returnValue(fibs));
			}
		});
		
		final List<Long> actual = goldenNuggetGenerator.generateNGoldenNuggets(n);
		final List<Long> expected = new ArrayList<>();
		expected.add(2l);
		expected.add(5l);
		expected.add(21l);
		expected.add(42l);
		expected.add(152l);
		assertEquals(expected, actual);
	}

}
