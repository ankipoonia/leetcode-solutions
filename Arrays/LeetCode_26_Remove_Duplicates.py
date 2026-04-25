class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Get the length of the input list
        l = len(nums)
        # Iterate from the end of the list to the beginning (index 1)
        # This allows safe removal of elements without index shifting issues
        for i in range(l-1, 0, -1):
            # Check if the current element is the same as the previous one
            if nums[i] == nums[i-1]:
                # Remove the duplicate element
                nums.pop(i)
        # Return the new length of the list after removing duplicates
        return len(nums)