from functools import lru_cache

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(start, end):
            # Initialize minimum cost to infinity
            min_cost = float("inf")
            
            # Try each possible cut position within this segment
            for cut in cuts:
                if start < cut < end:
                    # Cost is the length of current segment plus costs of left and right parts
                    cost = (end - start) + dfs(start, cut) + dfs(cut, end)
                    min_cost = min(min_cost, cost)
            
            # If no cuts were possible, return 0; otherwise return the minimum cost
            return 0 if min_cost == float("inf") else min_cost
        
        return dfs(0, n)