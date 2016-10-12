from individual import Individual
from match_results import MatchResults

permutation=[2,1,3]
matchResults = MatchResults()
matchResults.print(permutation)

print(matchResults.evaluate_permutation(permutation))
