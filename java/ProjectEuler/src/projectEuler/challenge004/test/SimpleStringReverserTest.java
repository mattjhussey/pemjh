/**
 * 
 */
package projectEuler.challenge004.test;

import static org.junit.Assert.assertEquals;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import projectEuler.challenge004.SimpleStringReverser;

/**
 * @author matt
 *
 */
public final class SimpleStringReverserTest {
	private final SimpleStringReverser stringReverser = new SimpleStringReverser();

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
	 * Test method for {@link projectEuler.challenge004.SimpleStringReverser#reverseString(java.lang.String)}.
	 */
	@Test
	public final void testReverseString() {
		String expected = "9876543210"; 
		String actual = stringReverser.reverseString("0123456789");
		assertEquals(expected, actual);
	}

}
