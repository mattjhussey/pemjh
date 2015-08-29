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

import projectEuler.challenge143.InvestigationBasedTriangle120PairFinder;
import projectEuler.utilities.factories.MapFactory;
import projectEuler.utilities.factories.SetFactory;

/**
 * @author matt
 *
 */
public class InvestigationBasedTriangle120PairFinderTest {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final MapFactory mapFactory = context.mock(MapFactory.class);
	private final SetFactory setFactory = context.mock(SetFactory.class);
	private final InvestigationBasedTriangle120PairFinder pairFinder = new InvestigationBasedTriangle120PairFinder(mapFactory, setFactory);

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
	 * Test method for {@link projectEuler.challenge143.InvestigationBasedTriangle120PairFinder#findPairsOfSidesLessThanN(int)}.
	 */
	@Test
	public final void testFindPairsOfSidesLessThanN() {
		final int n = 10;
		
		final Map<Integer, Set<Integer>> requestedMap = new HashMap<>();
		
		// Due to there only being one expected result, only one set is expected to be created
		final Set<Integer> requestedSet = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(mapFactory).createMap(); will(returnValue(requestedMap));
				oneOf(setFactory).createSet(); will(returnValue(requestedSet));
			}
		});
		
		final Map<Integer, Set<Integer>> actual = pairFinder.findPairsOfSidesLessThanN(n);		
		final Map<Integer, Set<Integer>> expected = new HashMap<Integer, Set<Integer>>();
		final Set<Integer> set3 = new HashSet<>();
		set3.add(5);
		expected.put(3, set3);
		
		assertEquals(expected, actual);
	}

}
