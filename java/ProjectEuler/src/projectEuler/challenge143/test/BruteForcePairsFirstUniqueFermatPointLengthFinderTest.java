/**
 * 
 */
package projectEuler.challenge143.test;

import static org.junit.Assert.assertEquals;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

import org.jmock.Expectations;
import org.jmock.integration.junit4.JUnitRuleMockery;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import projectEuler.challenge143.BruteForcePairsFirstUniqueFermatPointLengthFinder;
import projectEuler.challenge143.Triangle120PairFinder;
import projectEuler.utilities.factories.SetFactory;

/**
 * @author matt
 *
 */
public class BruteForcePairsFirstUniqueFermatPointLengthFinderTest {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final Triangle120PairFinder pairFinder = context.mock(Triangle120PairFinder.class);
	private final SetFactory setFactory = context.mock(SetFactory.class);
	private final BruteForcePairsFirstUniqueFermatPointLengthFinder lengthFinder = new BruteForcePairsFirstUniqueFermatPointLengthFinder(pairFinder, setFactory);

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
	 * Test method for {@link projectEuler.challenge143.BruteForcePairsFirstUniqueFermatPointLengthFinder#findUniqueFermatPointLengthsUpToN(int)}.
	 */
	@Test
	public final void testFindUniqueFermatPointLengthsUpToN() {
		final int n = 1000;

		final Map<Integer, Set<Integer>> pairs = new HashMap<Integer, Set<Integer>>();
		// 264 paired with 325
		final Set<Integer> pair264 = new HashSet<>();
		pair264.add(325);
		pairs.put(264, pair264);
		// 195 paired with 264 and 325
		final Set<Integer> pair195 = new HashSet<>();
		pair195.add(264);
		pair195.add(325);
		pairs.put(195, pair195);
		
		final Set<Integer> requestedSet = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(pairFinder).findPairsOfSidesLessThanN(n); will(returnValue(pairs));
				oneOf(setFactory).createSet(); will(returnValue(requestedSet));
			}
		});
		
		final Set<Integer> actual = lengthFinder.findUniqueFermatPointLengthsUpToN(n);
		final Set<Integer> expected = new HashSet<>();
		expected.add(784);
		
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge143.BruteForcePairsFirstUniqueFermatPointLengthFinder#findUniqueFermatPointLengthsUpToN(int)}.
	 */
	@Test
	public final void testFindUniqueFermatPointLengthsUpToN_55430() {
		// Testing an overflow situation where the proof algorithm squares the integers
		final int n = 55430;

		final Map<Integer, Set<Integer>> pairs = new HashMap<Integer, Set<Integer>>();
		// 10374 paired with 43680
		final Set<Integer> pair10374 = new HashSet<>();
		pair10374.add(43680);
		pairs.put(10374, pair10374);
		// 1376 paired with 10374 and 43680
		final Set<Integer> pair1376 = new HashSet<>();
		pair1376.add(10374);
		pair1376.add(43680);
		pairs.put(1376, pair1376);
		
		final Set<Integer> requestedSet = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(pairFinder).findPairsOfSidesLessThanN(n); will(returnValue(pairs));
				oneOf(setFactory).createSet(); will(returnValue(requestedSet));
			}
		});
		
		final Set<Integer> actual = lengthFinder.findUniqueFermatPointLengthsUpToN(n);
		final Set<Integer> expected = new HashSet<>();
		expected.add(55430);
		
		assertEquals(expected, actual);
	}

}
