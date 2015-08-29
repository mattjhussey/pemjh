/**
 * 
 */
package projectEuler.challenge004.test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.jmock.Expectations;
import org.jmock.integration.junit4.JUnitRuleMockery;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import projectEuler.challenge004.StringReverser;
import projectEuler.challenge004.StringReversingPalindromeValidator;

/**
 * @author matt
 *
 */
public final class StringReversingPalindromeValidatorTest {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final StringReverser stringReverser = context.mock(StringReverser.class);
	private final StringReversingPalindromeValidator palindromeValidator = new StringReversingPalindromeValidator(stringReverser);

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
	 * Test method for {@link projectEuler.challenge004.StringReversingPalindromeValidator#isPalindrome(int)}.
	 */
	@Test
	public final void testIsPalindromeSingleNumber() {
		// Single numbers are not palindromes
		boolean isPalindrome = palindromeValidator.isPalindrome(5);
		assertFalse(isPalindrome);
	}

	/**
	 * Test method for {@link projectEuler.challenge004.StringReversingPalindromeValidator#isPalindrome(int)}.
	 */
	@Test
	public final void testIsPalindromeOddNumber() {
		
		final String forward = "505";
		final String reversed = "505";
		
		context.checking(new Expectations() {
			{
				oneOf(stringReverser).reverseString(with(equal(forward))); will(returnValue(reversed));
			}
		});
		
		boolean isPalindrome = palindromeValidator.isPalindrome(505);
		assertTrue(isPalindrome);
	}

	/**
	 * Test method for {@link projectEuler.challenge004.StringReversingPalindromeValidator#isPalindrome(int)}.
	 */
	@Test
	public final void testIsPalindromeEvenNumber() {
		
		final String forward = "5005";
		final String reversed = "5005";
		
		context.checking(new Expectations() {
			{
				oneOf(stringReverser).reverseString(with(equal(forward))); will(returnValue(reversed));
			}
		});
		
		boolean isPalindrome = palindromeValidator.isPalindrome(5005);
		assertTrue(isPalindrome);
	}

}
