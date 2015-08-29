/**
 * 
 */
package projectEuler.challenge141.test;

import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

import org.jmock.Expectations;
import org.jmock.integration.junit4.JUnitRuleMockery;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Ignore;
import org.junit.Rule;
import org.junit.Test;

import projectEuler.challenge141.CutDownChallenge141;
import projectEuler.utilities.factories.ListFactory;
import projectEuler.utilities.factories.SetFactory;
import projectEuler.utilities.factories.SortedSetFactory;
import projectEuler.utilities.maths.PrimeGenerator;
import projectEuler.utilities.maths.SievePrimeGenerator;

/**
 * @author matt
 *
 */
@Ignore("Disabled since CFirstCutDownChallenge141 class supercedes this")
public final class CutDownChallenge141Test {
	@Rule public final JUnitRuleMockery context = new JUnitRuleMockery();
	private final PrimeGenerator generator = context.mock(PrimeGenerator.class);
	private final SetFactory setFactory = context.mock(SetFactory.class);
	private final CutDownChallenge141 challenge = new CutDownChallenge141(generator, setFactory);

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
	 * Test method for {@link projectEuler.challenge141.CutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_10() {
		final int n = 10;
		
		final int primeLimit = 4;
		
		final ListFactory listFactory = new ListFactory() {
			
			@Override
			public <T> List<T> createList() {
				return new ArrayList<>();
			}
		};
		
		final SortedSetFactory sortedSetFactory = new SortedSetFactory() {
			
			@Override
			public <T> SortedSet<T> createSortedSet() {
				return new TreeSet<>();
			}
		};
		
		final SievePrimeGenerator primeGenerator = new SievePrimeGenerator(listFactory, sortedSetFactory);
		
		final SortedSet<Integer> primes = primeGenerator.findPrimesUpToN(primeLimit);
		
		final Set<Long> set = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(generator).findPrimesUpToN(with(equal(primeLimit))); will(returnValue(primes));
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 9;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_100000() {
		final int n = 100000;
		
		final int primeLimit = 317;
		
		final ListFactory listFactory = new ListFactory() {
			
			@Override
			public <T> List<T> createList() {
				return new ArrayList<>();
			}
		};
		
		final SortedSetFactory sortedSetFactory = new SortedSetFactory() {
			
			@Override
			public <T> SortedSet<T> createSortedSet() {
				return new TreeSet<>();
			}
		};
		
		final SievePrimeGenerator primeGenerator = new SievePrimeGenerator(listFactory, sortedSetFactory);
		
		final SortedSet<Integer> primes = primeGenerator.findPrimesUpToN(primeLimit);
		
		final Set<Long> set = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(generator).findPrimesUpToN(with(equal(primeLimit))); will(returnValue(primes));
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 124657;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_1000000() {
		final int n = 1000000;
		
		final int primeLimit = 1001;
		
		final ListFactory listFactory = new ListFactory() {
			
			@Override
			public <T> List<T> createList() {
				return new ArrayList<>();
			}
		};
		
		final SortedSetFactory sortedSetFactory = new SortedSetFactory() {
			
			@Override
			public <T> SortedSet<T> createSortedSet() {
				return new TreeSet<>();
			}
		};
		
		final SievePrimeGenerator primeGenerator = new SievePrimeGenerator(listFactory, sortedSetFactory);
		
		final SortedSet<Integer> primes = primeGenerator.findPrimesUpToN(primeLimit);
		
		final Set<Long> set = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(generator).findPrimesUpToN(with(equal(primeLimit))); will(returnValue(primes));
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 700738;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_10000000() {
		final int n = 10000000;
		
		final int primeLimit = 3163;
		
		final ListFactory listFactory = new ListFactory() {
			
			@Override
			public <T> List<T> createList() {
				return new ArrayList<>();
			}
		};
		
		final SortedSetFactory sortedSetFactory = new SortedSetFactory() {
			
			@Override
			public <T> SortedSet<T> createSortedSet() {
				return new TreeSet<>();
			}
		};
		
		final SievePrimeGenerator primeGenerator = new SievePrimeGenerator(listFactory, sortedSetFactory);
		
		final SortedSet<Integer> primes = primeGenerator.findPrimesUpToN(primeLimit);
		
		final Set<Long> set = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(generator).findPrimesUpToN(with(equal(primeLimit))); will(returnValue(primes));
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 14253190;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_100000000() {
		final int n = 100000000;
		
		final int primeLimit = 10001;
		
		final ListFactory listFactory = new ListFactory() {
			
			@Override
			public <T> List<T> createList() {
				return new ArrayList<>();
			}
		};
		
		final SortedSetFactory sortedSetFactory = new SortedSetFactory() {
			
			@Override
			public <T> SortedSet<T> createSortedSet() {
				return new TreeSet<>();
			}
		};
		
		final SievePrimeGenerator primeGenerator = new SievePrimeGenerator(listFactory, sortedSetFactory);
		
		final SortedSet<Integer> primes = primeGenerator.findPrimesUpToN(primeLimit);
		
		final Set<Long> set = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(generator).findPrimesUpToN(with(equal(primeLimit))); will(returnValue(primes));
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 171436696;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_1000000000() {
		final int n = 1000000000;
		
		final int primeLimit = 31623;
		
		final ListFactory listFactory = new ListFactory() {
			
			@Override
			public <T> List<T> createList() {
				return new ArrayList<>();
			}
		};
		
		final SortedSetFactory sortedSetFactory = new SortedSetFactory() {
			
			@Override
			public <T> SortedSet<T> createSortedSet() {
				return new TreeSet<>();
			}
		};
		
		final SievePrimeGenerator primeGenerator = new SievePrimeGenerator(listFactory, sortedSetFactory);
		
		final SortedSet<Integer> primes = primeGenerator.findPrimesUpToN(primeLimit);
		
		final Set<Long> set = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(generator).findPrimesUpToN(with(equal(primeLimit))); will(returnValue(primes));
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 623708737;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_10000000000() {
		final long n = 10_000_000_000l;
		
		final int primeLimit = 100001;
		
		final ListFactory listFactory = new ListFactory() {
			
			@Override
			public <T> List<T> createList() {
				return new ArrayList<>();
			}
		};
		
		final SortedSetFactory sortedSetFactory = new SortedSetFactory() {
			
			@Override
			public <T> SortedSet<T> createSortedSet() {
				return new TreeSet<>();
			}
		};
		
		final SievePrimeGenerator primeGenerator = new SievePrimeGenerator(listFactory, sortedSetFactory);
		
		final SortedSet<Integer> primes = primeGenerator.findPrimesUpToN(primeLimit);
		
		final Set<Long> set = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(generator).findPrimesUpToN(with(equal(primeLimit))); will(returnValue(primes));
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 21630503507l;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_100000000000() {
		final long n = 100_000_000_000l;
		
		final int primeLimit = 316228;
		
		final ListFactory listFactory = new ListFactory() {
			
			@Override
			public <T> List<T> createList() {
				return new ArrayList<>();
			}
		};
		
		final SortedSetFactory sortedSetFactory = new SortedSetFactory() {
			
			@Override
			public <T> SortedSet<T> createSortedSet() {
				return new TreeSet<>();
			}
		};
		
		final SievePrimeGenerator primeGenerator = new SievePrimeGenerator(listFactory, sortedSetFactory);
		
		final SortedSet<Integer> primes = primeGenerator.findPrimesUpToN(primeLimit);
		
		final Set<Long> set = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(generator).findPrimesUpToN(with(equal(primeLimit))); will(returnValue(primes));
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 64431087395l;
		assertEquals(expected, actual);
	}

	/**
	 * Test method for {@link projectEuler.challenge141.CutDownChallenge141#findSumOfProgressiveSquaresBelowN(long)}.
	 */
	@Test
	public final void testFindSumOfProgressiveSquaresBelowN_1000000000000() {
		final long n = 1000_000_000_000l;
		
		final int primeLimit = 1000001;
		
		final ListFactory listFactory = new ListFactory() {
			
			@Override
			public <T> List<T> createList() {
				return new ArrayList<>();
			}
		};
		
		final SortedSetFactory sortedSetFactory = new SortedSetFactory() {
			
			@Override
			public <T> SortedSet<T> createSortedSet() {
				return new TreeSet<>();
			}
		};
		
		final SievePrimeGenerator primeGenerator = new SievePrimeGenerator(listFactory, sortedSetFactory);
		
		final SortedSet<Integer> primes = primeGenerator.findPrimesUpToN(primeLimit);
		
		final Set<Long> set = new HashSet<>();
		
		context.checking(new Expectations() {
			{
				oneOf(generator).findPrimesUpToN(with(equal(primeLimit))); will(returnValue(primes));
				oneOf(setFactory).createSet(); will(returnValue(set));
			}
		});
		
		final long actual = challenge.findSumOfProgressiveSquaresBelowN(n);
		final long expected = 878454337159l;
		assertEquals(expected, actual);
	}

}
