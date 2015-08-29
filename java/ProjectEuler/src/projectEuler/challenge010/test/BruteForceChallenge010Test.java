/**
 * 
 */
package projectEuler.challenge010.test;

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

import projectEuler.challenge010.BruteForceChallenge010;
import projectEuler.utilities.maths.PrimeGenerator;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge010Test {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final PrimeGenerator primeGenerator = context.mock(PrimeGenerator.class);
	private final BruteForceChallenge010 challenge = new BruteForceChallenge010(primeGenerator);

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
	 * Test method for {@link projectEuler.challenge010.BruteForceChallenge010#findSumOfAllPrimesUpToN(int)}.
	 */
	@Test
	public final void testFindSumOfAllPrimesUpToN() {
		
		final int n = 10;
		final SortedSet<Integer> primes = new TreeSet<>();
		primes.add(2);
		primes.add(3);
		primes.add(5);
		primes.add(7);
		
		context.checking(new Expectations() {
			{
				oneOf(primeGenerator).findPrimesUpToN(n); will(returnValue(primes));
			}
		});
		
		long actual = challenge.findSumOfAllPrimesUpToN(n);
		int expected = 17;
		assertEquals(expected, actual);
	}

}
