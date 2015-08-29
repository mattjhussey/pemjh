/**
 * 
 */
package projectEuler.utilities.maths.test;

import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
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

import projectEuler.utilities.factories.ListFactory;
import projectEuler.utilities.factories.SortedSetFactory;
import projectEuler.utilities.maths.SievePrimeGenerator;

/**
 * @author matt
 *
 */
public final class SievePrimeGeneratorTest {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final ListFactory listFactory = context.mock(ListFactory.class);
	private final SortedSetFactory sortedSetFactory = context.mock(SortedSetFactory.class);
	private final SievePrimeGenerator primeGenerator = new SievePrimeGenerator(listFactory, sortedSetFactory);

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
	 * Test method for {@link projectEuler.utilities.maths.SievePrimeGenerator#findPrimesUpToN(int)}.
	 */
	@Test
	public final void testFindPrimesUpToN() {
		
		final List<Boolean> list = new LinkedList<>();
		final SortedSet<Integer> sortedSet = new TreeSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(listFactory).createList(); will(returnValue(list));
				oneOf(sortedSetFactory).createSortedSet(); will(returnValue(sortedSet));
			}
		});
		
		final SortedSet<Integer> primes = primeGenerator.findPrimesUpToN(20);
		final List<Integer> primeList = Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19); 
		final SortedSet<Integer> expected = new TreeSet<>(primeList);
		
		assertEquals(expected, primes);
	}

}
