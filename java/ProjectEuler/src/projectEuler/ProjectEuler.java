/**
 * 
 */
package projectEuler;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.SortedMap;
import java.util.SortedSet;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

import org.picocontainer.DefaultPicoContainer;
import org.picocontainer.MutablePicoContainer;
import org.picocontainer.Parameter;
import org.picocontainer.PicoBuilder;
import org.picocontainer.parameters.ComponentParameter;
import org.picocontainer.parameters.ConstantParameter;

import projectEuler.challenge001.Challenge001BruteForce;
import projectEuler.challenge001.Challenge001Caller;
import projectEuler.challenge002.Challenge002BruteForce;
import projectEuler.challenge002.Challenge002Caller;
import projectEuler.challenge003.Challenge003BruteForce;
import projectEuler.challenge003.Challenge003Caller;
import projectEuler.challenge004.Challenge004Caller;
import projectEuler.challenge004.Challenge004Filtered;
import projectEuler.challenge004.SimpleRangeFinder;
import projectEuler.challenge004.SimpleStringReverser;
import projectEuler.challenge004.StringReversingPalindromeValidator;
import projectEuler.challenge005.Challenge005Caller;
import projectEuler.challenge005.PrimeFactorChallenge005;
import projectEuler.challenge006.Challenge006Caller;
import projectEuler.challenge006.ClosedFunctionSumFinder;
import projectEuler.challenge006.ClosedFunctionSumOfSquaresFinder;
import projectEuler.challenge006.SimpleChallenge006;
import projectEuler.challenge007.BruteForceChallenge007;
import projectEuler.challenge007.Challenge007Caller;
import projectEuler.challenge008.BruteForceChallenge008;
import projectEuler.challenge008.Challenge008Caller;
import projectEuler.challenge009.BruteForceChallenge009;
import projectEuler.challenge009.Challenge009Caller;
import projectEuler.challenge010.BruteForceChallenge010;
import projectEuler.challenge010.Challenge010Caller;
import projectEuler.challenge140.BruteForceChallenge140;
import projectEuler.challenge140.BruteForceFibonnaciGenerator;
import projectEuler.challenge140.BruteForceGoldenNuggetGenerator;
import projectEuler.challenge140.Challenge140Caller;
import projectEuler.challenge141.CFirstCutDownChallenge141;
import projectEuler.challenge141.Challenge141Caller;
import projectEuler.challenge143.BruteForceChallenge143;
import projectEuler.challenge143.BruteForcePairsFirstUniqueFermatPointLengthFinder;
import projectEuler.challenge143.Challenge143Caller;
import projectEuler.challenge143.InvestigationBasedTriangle120PairFinder;
import projectEuler.challenge147.BruteForceAlignedRectangleFinder;
import projectEuler.challenge147.BruteForceChallenge147;
import projectEuler.challenge147.BruteForceDiagonalRectangleFinder;
import projectEuler.challenge147.Challenge147Caller;
import projectEuler.challenge150.ArrayChallengeTriangle;
import projectEuler.challenge150.BruteForceChallenge150;
import projectEuler.challenge150.Challenge150Caller;
import projectEuler.utilities.factories.PicoListFactory;
import projectEuler.utilities.factories.PicoMapFactory;
import projectEuler.utilities.factories.PicoSetFactory;
import projectEuler.utilities.factories.PicoSortedSetFactory;
import projectEuler.utilities.maths.SievePrimeGenerator;

/**
 * @author matt
 *
 */
public class ProjectEuler {

	/**
	 * @param args
	 * @throws InterruptedException 
	 * @throws ExecutionException 
	 */
	public static void main(String[] args) throws InterruptedException, ExecutionException {
		
		//final List<Callable<String>> tasks = createHandRolledTasks();
		final List<Callable<String>> tasks = createPicocontainerTasks();
		
		final int threads = 4;
		
		ExecutorService ex = Executors.newFixedThreadPool(threads);
		
		for(Future<String> result: ex.invokeAll(tasks)) {
			System.out.println(result.get());
		}
		
		ex.shutdown();
	}
	
	private static List<Callable<String>> createPicocontainerTasks() {
		
		MutablePicoContainer basePicoContainer = new DefaultPicoContainer();
		basePicoContainer.addComponent(List.class, ArrayList.class, Parameter.ZERO);
		basePicoContainer.addComponent(SortedMap.class, TreeMap.class, Parameter.ZERO);
		basePicoContainer.addComponent(SortedSet.class, TreeSet.class, Parameter.ZERO);
		basePicoContainer.addComponent(Map.class, HashMap.class, Parameter.ZERO);
		basePicoContainer.addComponent(Set.class, HashSet.class, Parameter.ZERO);
		
		MutablePicoContainer cachedToolsPicocontainer = new PicoBuilder(basePicoContainer).withCaching().build();
		cachedToolsPicocontainer.addComponent(SimpleStringReverser.class);
		cachedToolsPicocontainer.addComponent(StringReversingPalindromeValidator.class);
		cachedToolsPicocontainer.addComponent(SimpleRangeFinder.class);
		cachedToolsPicocontainer.addComponent(SievePrimeGenerator.class);
		cachedToolsPicocontainer.addComponent(ClosedFunctionSumFinder.class);
		cachedToolsPicocontainer.addComponent(ClosedFunctionSumOfSquaresFinder.class);
		cachedToolsPicocontainer.addComponent(BruteForceGoldenNuggetGenerator.class);
		cachedToolsPicocontainer.addComponent(BruteForceFibonnaciGenerator.class);
		cachedToolsPicocontainer.addComponent(InvestigationBasedTriangle120PairFinder.class);
		cachedToolsPicocontainer.addComponent(BruteForcePairsFirstUniqueFermatPointLengthFinder.class);
		cachedToolsPicocontainer.addComponent(BruteForceAlignedRectangleFinder.class);
		cachedToolsPicocontainer.addComponent(BruteForceDiagonalRectangleFinder.class);
		cachedToolsPicocontainer.addComponent(ArrayChallengeTriangle.class);
		
		cachedToolsPicocontainer.addComponent(PicoMapFactory.class);
		cachedToolsPicocontainer.addComponent(PicoSortedSetFactory.class);
		cachedToolsPicocontainer.addComponent(PicoListFactory.class);
		cachedToolsPicocontainer.addComponent(PicoSetFactory.class);
		
		cachedToolsPicocontainer.addComponent(Challenge001BruteForce.class);
		cachedToolsPicocontainer.addComponent(Challenge002BruteForce.class);
		cachedToolsPicocontainer.addComponent(Challenge003BruteForce.class);
		cachedToolsPicocontainer.addComponent(Challenge004Filtered.class);
		cachedToolsPicocontainer.addComponent(PrimeFactorChallenge005.class);
		cachedToolsPicocontainer.addComponent(SimpleChallenge006.class);
		cachedToolsPicocontainer.addComponent(BruteForceChallenge007.class);
		cachedToolsPicocontainer.addComponent(BruteForceChallenge008.class);
		cachedToolsPicocontainer.addComponent(BruteForceChallenge009.class);
		cachedToolsPicocontainer.addComponent(BruteForceChallenge010.class);
		cachedToolsPicocontainer.addComponent(BruteForceChallenge140.class);
		cachedToolsPicocontainer.addComponent(CFirstCutDownChallenge141.class);
		cachedToolsPicocontainer.addComponent(BruteForceChallenge143.class);
		cachedToolsPicocontainer.addComponent(BruteForceChallenge147.class);
		cachedToolsPicocontainer.addComponent(BruteForceChallenge150.class);
		
		// If any Maps want a picocontainer then they can have the cached one, and hence the base.
		// If any need a specific picocontainer then they can configure that later.
		cachedToolsPicocontainer.addComponent(cachedToolsPicocontainer);
		
		@SuppressWarnings("unchecked")
		final SortedMap<String, Class<? extends Challenge>> unwrappedChallenges = cachedToolsPicocontainer.getComponent(SortedMap.class);
		
		// Challenges
		unwrappedChallenges.put("Challenge001", Challenge001Caller.class);
		unwrappedChallenges.put("Challenge002", Challenge002Caller.class);
		unwrappedChallenges.put("Challenge003", Challenge003Caller.class);
		unwrappedChallenges.put("Challenge004", Challenge004Caller.class);
		unwrappedChallenges.put("Challenge005", Challenge005Caller.class);
		unwrappedChallenges.put("Challenge006", Challenge006Caller.class);
		unwrappedChallenges.put("Challenge007", Challenge007Caller.class);
		unwrappedChallenges.put("Challenge008", Challenge008Caller.class);
		unwrappedChallenges.put("Challenge009", Challenge009Caller.class);
		unwrappedChallenges.put("Challenge010", Challenge010Caller.class);
		unwrappedChallenges.put("Challenge140", Challenge140Caller.class);
		unwrappedChallenges.put("Challenge141", Challenge141Caller.class);
		unwrappedChallenges.put("Challenge143", Challenge143Caller.class);
		unwrappedChallenges.put("Challenge147", Challenge147Caller.class);
		unwrappedChallenges.put("Challenge150", Challenge150Caller.class);

		@SuppressWarnings("unchecked")
		final List<Callable<String>> tasks = cachedToolsPicocontainer.getComponent(List.class);
		
		
		for(Entry<String, Class<? extends Challenge>> challenge: unwrappedChallenges.entrySet()) {
			MutablePicoContainer challengePicocontainer = cachedToolsPicocontainer.makeChildContainer();
			challengePicocontainer.addComponent(challenge.getValue());
			
			MutablePicoContainer timingPicocontainer = challengePicocontainer.makeChildContainer();
			timingPicocontainer.addComponent(ChallengeTimer.class);
			
			MutablePicoContainer labellingPicoContainer = timingPicocontainer.makeChildContainer();
			labellingPicoContainer.addComponent(Challenge.class, ChallengeLabeller.class, new ComponentParameter(), new ConstantParameter(challenge.getKey()));
			
			tasks.add(labellingPicoContainer.getComponent(Challenge.class));
		}
		
		return tasks;
	}

}
