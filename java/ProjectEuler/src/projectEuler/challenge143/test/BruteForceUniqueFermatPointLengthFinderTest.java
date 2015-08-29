/**
 * 
 */
package projectEuler.challenge143.test;

import static org.junit.Assert.*;

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

import projectEuler.challenge143.BruteForceUniqueFermatPointLengthFinder;
import projectEuler.challenge143.Triangle120SideVerifier;
import projectEuler.utilities.factories.SetFactory;

/**
 * @author matt
 *
 */
public class BruteForceUniqueFermatPointLengthFinderTest {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final SetFactory setFactory = context.mock(SetFactory.class);
	private final Triangle120SideVerifier verifier = context.mock(Triangle120SideVerifier.class);
	private final BruteForceUniqueFermatPointLengthFinder lengthFinder = new BruteForceUniqueFermatPointLengthFinder(setFactory, verifier);

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
	 * Test method for {@link projectEuler.challenge143.BruteForceUniqueFermatPointLengthFinder#findUniqueFermatPointLengthsUpToN(int)}.
	 */
	@Test
	public final void testFindUniqueFermatPointLengthsUpToN() {
		final int n = 15;
		
		final Set<Integer> requestedSet = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(setFactory).createSet(); will(returnValue(requestedSet));
				
				oneOf(verifier).areShortSidesOf120DegTriangle(3, 5); will(returnValue(true));
				oneOf(verifier).areShortSidesOf120DegTriangle(3, 7); will(returnValue(true));
				oneOf(verifier).areShortSidesOf120DegTriangle(5, 7); will(returnValue(true));
				
				allowing(verifier).areShortSidesOf120DegTriangle(with(any(Integer.class)), with(any(Integer.class))); will(returnValue(false));
			}
		});
		
		final Set<Integer> actual = lengthFinder.findUniqueFermatPointLengthsUpToN(n);
		final Set<Integer> expected = new HashSet<>();
		expected.add(15);
		
		assertEquals(expected, actual);
	}

}
