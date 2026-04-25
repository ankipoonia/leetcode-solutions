class Solution:
    def jump(self, nums: List[int]) -> int:
        # End of current jump range
        currEnd = 0
        # Farthest index reachable so far
        canJump = 0
        # Number of jumps made
        jumpCount = 0
        for i in range(len(nums)-1):
            # Update farthest reachable index from current position
            canJump = max(canJump, nums[i] + i)
            # When we reach the end of current jump range, make a jump
            if i == currEnd:
                currEnd = canJump
                jumpCount += 1
        return jumpCount