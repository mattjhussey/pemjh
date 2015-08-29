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

import projectEuler.challenge004.Challenge004BruteForce;
import projectEuler.challenge004.PalindromeValidator;
import projectEuler.challenge004.Range;
import projectEuler.challenge004.RangeFinder;

/**
 * @author matt
 *
 */
public final class Challenge004BruteForceTest {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final PalindromeValidator palindromeValidator = context.mock(PalindromeValidator.class);
	private final RangeFinder rangeFinder = context.mock(RangeFinder.class);
	private final Challenge004BruteForce challenge = new Challenge004BruteForce(palindromeValidator, rangeFinder);

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
	 * Test method for {@link projectEuler.challenge004.Challenge004BruteForce#getLargestPalindromeOfDigitProduct(int)}.
	 */
	@Test
	public final void testGetLargestPalindromeOfDigitProduct() {
		
		final Range range = context.mock(Range.class);
		final int maximum = 4;
		final int minimum = 2;
		
		final int p1 = 4; // is palindrome
		final int p2 = 6; // is palindrome
		final int p3 = 9; // is not palindrome
		
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
		final int expected = 6;
		assertEquals(expected, actual);
	}

}
