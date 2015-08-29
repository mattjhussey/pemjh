/**
 * 
 */
package projectEuler.challenge143.test;

import static org.junit.Assert.*;

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

import projectEuler.challenge143.BruteForceTriangle120PairFinder;
import projectEuler.challenge143.Triangle120SideVerifier;
import projectEuler.utilities.factories.MapFactory;
import projectEuler.utilities.factories.SetFactory;

/**
 * @author matt
 *
 */
public class BruteForceTriangle120PairFinderTest {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final MapFactory mapFactory = context.mock(MapFactory.class);
	private final SetFactory setFactory = context.mock(SetFactory.class);
	private final Triangle120SideVerifier verifier = context.mock(Triangle120SideVerifier.class);
	private final BruteForceTriangle120PairFinder pairFinder = new BruteForceTriangle120PairFinder(mapFactory, setFactory, verifier);

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
	 * Test method for {@link projectEuler.challenge143.BruteForceTriangle120PairFinder#findPairsOfSidesLessThanN(int)}.
	 */
	@Test
	public final void testFindPairsOfSidesLessThanN() {
		final int n = 10;
		
		final Map<Integer, Set<Integer>> requestedMap = new HashMap<>();
		
		final Set<Integer> requestedSet = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				// Map and Sets for returning results
				oneOf(mapFactory).createMap(); will(returnValue(requestedMap));
				oneOf(setFactory).createSet(); will(returnValue(requestedSet));
				
				// Only valid results for testing
				oneOf(verifier).areShortSidesOf120DegTriangle(with(equal(3)), with(equal(5))); will(returnValue(true));
				
				// All other validations are invalid as far as we are concerned
				allowing(verifier).areShortSidesOf120DegTriangle(with(any(Integer.class)), with(any(Integer.class))); will(returnValue(false));
			}
		});
		
		final Map<Integer, Set<Integer>> actual = pairFinder.findPairsOfSidesLessThanN(n);
		final Map<Integer, Set<Integer>> expected = new HashMap<Integer, Set<Integer>>();
		final Set<Integer> pair3 = new HashSet<>();
		pair3.add(5);
		expected.put(3, pair3);
		
		assertEquals(expected, actual);
	}

}
