package projectEuler.challenge140.test;

import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.List;

import org.jmock.Expectations;
import org.jmock.integration.junit4.JUnitRuleMockery;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import projectEuler.challenge140.BruteForceFibonnaciGenerator;
import projectEuler.utilities.factories.ListFactory;

public final class BruteForceFibonnaciGeneratorTest {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final ListFactory listFactory = context.mock(ListFactory.class);
	private final BruteForceFibonnaciGenerator fibonacciGenerator = new BruteForceFibonnaciGenerator(listFactory);

	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
	}

	@AfterClass
	public static void tearDownAfterClass() throws Exception {
	}

	@Before
	public void setUp() throws Exception {
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public final void testGenerateNFibonacciNumbers() {
		final int n = 10;
		
		final List<Integer> list = new ArrayList<>();
		
		context.checking(new Expectations() {
			{
				oneOf(listFactory).createList(); will(returnValue(list));
			}
		});
		
		final List<Long> actual = fibonacciGenerator.generateNFibonacciNumbers(n);
		final List<Long> expected = new ArrayList<>();
		expected.add(1l);
		expected.add(2l);
		expected.add(3l);
		expected.add(5l);
		expected.add(8l);
		expected.add(13l);
		expected.add(21l);
		expected.add(34l);
		expected.add(55l);
		expected.add(89l);
		
		assertEquals(expected, actual);
	}

}
