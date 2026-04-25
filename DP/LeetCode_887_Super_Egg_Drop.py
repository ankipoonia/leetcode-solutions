from functools import lru_cache

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        Find the minimum number of moves to determine the highest floor from which 
        an egg won't break when dropped, given k eggs and n floors.
        
        Args:
            k: Number of eggs available
            n: Number of floors in the building
            
        Returns:
            Minimum number of moves required in the worst case
        """
        @lru_cache(maxsize=None)
        def dfs(eggs, floors):
            # Base cases: no eggs or no floors means no moves needed
            if eggs == 0 or floors == 0: 
                return 0
            
            # The number of floors we can cover with current eggs and floors
            # is 1 (current floor) + floors covered if egg breaks + floors covered if egg doesn't break
            return 1 + dfs(eggs-1, floors-1) + dfs(eggs, floors-1)
        
        # f represents the maximum floors we can cover with current moves
        # m represents the number of moves
        f, m = 0, 0
        
        # Keep increasing moves until we can cover at least n floors
        while f < n:
            f = dfs(k, m)
            m += 1
        
        # Return the minimum moves needed (m-1 because we incremented m after finding the solution)
        return m - 1