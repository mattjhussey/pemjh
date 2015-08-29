/**
 * 
 */
package projectEuler.challenge143.test;

import static org.junit.Assert.assertEquals;

import java.util.HashSet;
import java.util.Set;

import org.jmock.Expectations;
import org.jmock.integration.junit4.JUnitRuleMockery;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import projectEuler.challenge143.BruteForceChallenge143;
import projectEuler.challenge143.UniqueFermatPointLengthFinder;

/**
 * @author matt
 *
 */
public class BruteForceChallenge143Test {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final UniqueFermatPointLengthFinder lengthFinder = context.mock(UniqueFermatPointLengthFinder.class);
	private final BruteForceChallenge143 challenge = new BruteForceChallenge143(lengthFinder);

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
	 * Test method for {@link projectEuler.challenge143.BruteForceChallenge143#findFermatPointSumsUpToN(int)}.
	 */
	@Test
	public final void testFindFermatPointSumsUpToN() {
		final Integer n = 5;
		
		final Set<Integer> lengths = new HashSet<>();
		lengths.add(1);
		lengths.add(2);
		lengths.add(3);
		lengths.add(4);
		lengths.add(5);
		
		context.checking(new Expectations() {
			{
				oneOf(lengthFinder).findUniqueFermatPointLengthsUpToN(with(equal(n))); will(returnValue(lengths));
			}
		});
		
		final long actual = challenge.findFermatPointSumsUpToN(n);
		final long expected = 15;
		assertEquals(expected, actual);
	}

}
