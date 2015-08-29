/**
 * 
 */
package projectEuler.challenge005.test;

import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
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

import projectEuler.challenge005.PrimeFactorChallenge005;
import projectEuler.utilities.factories.MapFactory;
import projectEuler.utilities.maths.PrimeGenerator;

/**
 * @author matt
 *
 */
public final class PrimeFactorChallenge005Test {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final PrimeGenerator primeGenerator = context.mock(PrimeGenerator.class);
	private final MapFactory mapFactory = context.mock(MapFactory.class);
	private final PrimeFactorChallenge005 challenge = new PrimeFactorChallenge005(primeGenerator, mapFactory);
	
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
	 * Test method for {@link projectEuler.challenge005.PrimeFactorChallenge005#findLowestCommonDenominatorOfNumsUpToN(int)}.
	 */
	@Test
	public final void testFindLowestCommonDenominatorOfNumsUpToN() {
		
		final int n = 10;
		final List<Integer> primeList = Arrays.asList(2, 3, 5, 7);
		final SortedSet<Integer> primes = new TreeSet<>(primeList);
		final Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		
		context.checking(new Expectations() {
			{
				oneOf(primeGenerator).findPrimesUpToN(n); will(returnValue(primes));
				oneOf(mapFactory).createMap(); will(returnValue(map));
			}
		});
		
		int lcd = challenge.findLowestCommonDenominatorOfNumsUpToN(n);
		int expected = 2520;
		assertEquals(expected, lcd);
	}

}
