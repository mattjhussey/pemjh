/**
 * 
 */
package projectEuler.challenge007.test;

import static org.junit.Assert.assertEquals;

import java.util.SortedSet;
import java.util.TreeSet;

import org.jmock.Expectations;
import org.jmock.integration.junit4.JUnitRuleMockery;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import projectEuler.challenge007.BruteForceChallenge007;
import projectEuler.utilities.factories.SortedSetFactory;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge007Test {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final SortedSetFactory sortedSetFactory = context.mock(SortedSetFactory.class);
	private final BruteForceChallenge007 challenge = new BruteForceChallenge007(sortedSetFactory);

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
	 * Test method for {@link projectEuler.challenge007.BruteForceChallenge007#findNthPrime(int)}.
	 */
	@Test
	public final void testFindNthPrime() {
		
		final SortedSet<Integer> sortedSet = new TreeSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(sortedSetFactory).createSortedSet(); will(returnValue(sortedSet));
			}
		});
		
		final int n = 6;
		final int actual = challenge.findNthPrime(n);
		final int expected = 13;
		assertEquals(expected, actual);
	}

}
