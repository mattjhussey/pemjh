/**
 * 
 */
package projectEuler.challenge140;

import java.util.List;

/**
 * @author matt
 *
 */
public final class BruteForceChallenge140 implements Challenge140 {
	
	public BruteForceChallenge140(GoldenNuggetGenerator generator) {
		this.generator = generator;
	}

	/* (non-Javadoc)
	 * @see projectEuler.challenge140.Challenge140#findSumOfFirstNNuggets(int)
	 */
	@Override
	public long findSumOfFirstNNuggets(int n) {
		
		List<Long> nuggets = generator.generateNGoldenNuggets(n);
		
		long total = 0;
		
		for(Long nugget: nuggets) {
			total += nugget;
		}
		
		return total;
	}
	
	private final GoldenNuggetGenerator generator;

}
