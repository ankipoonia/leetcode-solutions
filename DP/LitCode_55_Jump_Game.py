class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Track the maximum index we can reach from the starting position
        canJump = 1 # Start with 1 because we can jump from the first position
        for num in nums:
            # If max reachable index is before current position, we're stuck
            if canJump - 1 < 0: return False
            # Update max reachable index: either jump length from current position or previous max
            canJump = max(num, canJump-1)
        return True