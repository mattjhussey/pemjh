/**
 * 
 */
package projectEuler.challenge141.test;

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

import projectEuler.challenge141.CFirstCutDownChallenge141;
import projectEuler.utilities.factories.SetFactory;

/**
 * @author matt
 *
 */
public final class CFirstCutDownChallenge141Test {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final SetFactory setFactory = context.mock(SetFactory.class);
	private final CFirstCutDownChallenge141 challenge = new CFirstCutDownChallenge141(setFactory);

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
	 * Test method for {@link projectEuler.challenge141.CFirstCutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_10() {
		final int n = 10;		
		
		final Set<Long> set = new HashSet<>(); 
		
		context.checking(new Expectations() {
			{
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 9;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CFirstCutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_100000() {
		final int n = 100000;	
		
		final Set<Long> set = new HashSet<>(); 
		
		context.checking(new Expectations() {
			{
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 124657;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CFirstCutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_1000000() {
		final int n = 1000000;	
		
		final Set<Long> set = new HashSet<>(); 
		
		context.checking(new Expectations() {
			{
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 700738;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CFirstCutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_10000000() {
		final int n = 10000000;	
		
		final Set<Long> set = new HashSet<>(); 
		
		context.checking(new Expectations() {
			{
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 14253190;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CFirstCutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_100000000() {
		final int n = 100000000;
		
		final Set<Long> set = new HashSet<>(); 
		
		context.checking(new Expectations() {
			{
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 171436696;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CFirstCutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_1000000000() {
		final int n = 1000000000;
		
		final Set<Long> set = new HashSet<>(); 
		
		context.checking(new Expectations() {
			{
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 623708737;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CFirstCutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_10000000000() {
		final long n = 10_000_000_000l;	
		
		final Set<Long> set = new HashSet<>(); 
		
		context.checking(new Expectations() {
			{
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 21630503507l;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CFirstCutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_100000000000() {
		final long n = 100_000_000_000l;	
		
		final Set<Long> set = new HashSet<>(); 
		
		context.checking(new Expectations() {
			{
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 64431087395l;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CFirstCutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_1000000000000() {
		final long n = 1000_000_000_000l;	
		
		final Set<Long> set = new HashSet<>(); 
		
		context.checking(new Expectations() {
			{
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 878454337159l;
		assertEquals(expected, actual);
	}

}
