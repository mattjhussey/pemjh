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

import projectEuler.challenge004.Challenge004Filtered;
import projectEuler.challenge004.Challenge004StopEarly;
import projectEuler.challenge004.PalindromeValidator;
import projectEuler.challenge004.Range;
import projectEuler.challenge004.RangeFinder;
import projectEuler.challenge004.SimpleRangeFinder;
import projectEuler.challenge004.SimpleStringReverser;
import projectEuler.challenge004.StringReverser;
import projectEuler.challenge004.StringReversingPalindromeValidator;

/**
 * @author matt
 *
 */
public final class Challenge004FilteredTest {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final PalindromeValidator palindromeValidator = context.mock(PalindromeValidator.class);
	private final RangeFinder rangeFinder = context.mock(RangeFinder.class);
	private final Challenge004Filtered challenge = new Challenge004Filtered(palindromeValidator, rangeFinder);

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
	 * Test method for {@link projectEuler.challenge004.Challenge004Filtered#getLargestPalindromeOfDigitProduct(int)}.
	 */
	@Test
	public final void testGetLargestPalindromeOfDigitProduct() {
		
		final Range range = context.mock(Range.class);
		// Filtered optimisation approach requires these numbers to include an 11 else the algorithm assumes there are no palindromes
		final int maximum = 12;
		final int minimum = 10;
		
		final int p1 = 100; // is palindrome
		final int p2 = 110; // is palindrome
		final int p3 = 121; // is not palindrome
		
		context.checking(new Expectations()
		{
			{
				allowing(range).getMaximum(); will(returnValue(maximum));
				allowing(range).getMinimum(); will(returnValue(minimum));
				
				oneOf(rangeFinder).findRangeWithNDigits(2); will(returnValue(range));
				
				allowing(palindromeValidator).isPalindrome(with(equal(p1))); will(returnValue(true));
				allowing(palindromeValidator).isPalindrome(with(equal(p2))); will(returnValue(true));
				allowing(palindromeValidator).isPalindrome(with(equal(p3))); will(returnValue(false));
			}
		});
		
		final int actual = challenge.getLargestPalindromeOfDigitProduct(2);
		final int expected = 110;
		assertEquals(expected, actual);
	}
	
	/**
	 * Test against the Stop Early version, which I am confident works well
	 */
	@Test
	public final void testAgainstKnown() {
		final StringReverser stringReverser = new SimpleStringReverser();
		final PalindromeValidator palindromeValidator = new StringReversingPalindromeValidator(stringReverser);
		final RangeFinder rangeFinder = new SimpleRangeFinder();
		
		final Challenge004Filtered filtered = new Challenge004Filtered(palindromeValidator, rangeFinder);
		final Challenge004StopEarly bruteForce = new Challenge004StopEarly(palindromeValidator, rangeFinder);
		
		for(int n = 0; n != 5; ++n) {
			int known = bruteForce.getLargestPalindromeOfDigitProduct(n);
			int actual = filtered.getLargestPalindromeOfDigitProduct(n);
			
			assertEquals(known, actual);
		}
	}

}
