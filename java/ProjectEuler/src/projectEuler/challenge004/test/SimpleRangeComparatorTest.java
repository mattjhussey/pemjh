/**
 * 
 */
package projectEuler.challenge004.test;

import static org.junit.Assert.assertEquals;

import org.jmock.Expectations;
import org.jmock.integration.junit4.JUnitRuleMockery;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import projectEuler.challenge004.Range;
import projectEuler.challenge004.SimpleRangeComparator;

/**
 * @author matt
 *
 */
public final class SimpleRangeComparatorTest {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final SimpleRangeComparator comparator = new SimpleRangeComparator();

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
	 * Test method for {@link projectEuler.challenge004.SimpleRangeComparator#compare(projectEuler.challenge004.Range, projectEuler.challenge004.Range)}.
	 */
	@Test
	public final void testCompareEqual() {
		final int maximums = 5;
		final int minimums = 3;
		
		final Range arg0 = context.mock(Range.class, "Arg0");
		final Range arg1 = context.mock(Range.class, "Arg1");
		
		context.checking(new Expectations() {
			{
				oneOf(arg0).getMinimum(); will(returnValue(minimums));
				oneOf(arg0).getMaximum(); will(returnValue(maximums));
				oneOf(arg1).getMinimum(); will(returnValue(minimums));
				oneOf(arg1).getMaximum(); will(returnValue(maximums));
			}
		});

		final int expected = 0;
		final int actual = comparator.compare(arg0, arg1);
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge004.SimpleRangeComparator#compare(projectEuler.challenge004.Range, projectEuler.challenge004.Range)}.
	 */
	@Test
	public final void testCompareMax0Greater() {
		final int arg0maximum = 5;
		final int arg1maximum = 3;
		
		final Range arg0 = context.mock(Range.class, "Arg0");
		final Range arg1 = context.mock(Range.class, "Arg1");
		
		context.checking(new Expectations() {
			{
				oneOf(arg0).getMaximum(); will(returnValue(arg0maximum));
				oneOf(arg1).getMaximum(); will(returnValue(arg1maximum));
			}
		});

		final int expected = 1;
		final int actual = comparator.compare(arg0, arg1);
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge004.SimpleRangeComparator#compare(projectEuler.challenge004.Range, projectEuler.challenge004.Range)}.
	 */
	@Test
	public final void testCompareMax0Less() {
		final int arg0maximum = 3;
		final int arg1maximum = 5;
		
		final Range arg0 = context.mock(Range.class, "Arg0");
		final Range arg1 = context.mock(Range.class, "Arg1");
		
		context.checking(new Expectations() {
			{
				oneOf(arg0).getMaximum(); will(returnValue(arg0maximum));
				oneOf(arg1).getMaximum(); will(returnValue(arg1maximum));
			}
		});

		final int expected = -1;
		final int actual = comparator.compare(arg0, arg1);
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge004.SimpleRangeComparator#compare(projectEuler.challenge004.Range, projectEuler.challenge004.Range)}.
	 */
	@Test
	public final void testCompareMin0Greater() {
		final int maximums = 4;
		final int arg0minimum = 5;
		final int arg1minimum = 3;
		
		final Range arg0 = context.mock(Range.class, "Arg0");
		final Range arg1 = context.mock(Range.class, "Arg1");
		
		context.checking(new Expectations() {
			{
				oneOf(arg0).getMinimum(); will(returnValue(arg0minimum));
				oneOf(arg0).getMaximum(); will(returnValue(maximums));
				oneOf(arg1).getMinimum(); will(returnValue(arg1minimum));
				oneOf(arg1).getMaximum(); will(returnValue(maximums));
			}
		});

		final int expected = 1;
		final int actual = comparator.compare(arg0, arg1);
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge004.SimpleRangeComparator#compare(projectEuler.challenge004.Range, projectEuler.challenge004.Range)}.
	 */
	@Test
	public final void testCompareMin0Less() {
		final int maximums = 4;
		final int arg0minimum = 3;
		final int arg1minimum = 5;
		
		final Range arg0 = context.mock(Range.class, "Arg0");
		final Range arg1 = context.mock(Range.class, "Arg1");
		
		context.checking(new Expectations() {
			{
				oneOf(arg0).getMinimum(); will(returnValue(arg0minimum));
				oneOf(arg0).getMaximum(); will(returnValue(maximums));
				oneOf(arg1).getMinimum(); will(returnValue(arg1minimum));
				oneOf(arg1).getMaximum(); will(returnValue(maximums));
			}
		});

		final int expected = -1;
		final int actual = comparator.compare(arg0, arg1);
		assertEquals(expected, actual);
	}

}
