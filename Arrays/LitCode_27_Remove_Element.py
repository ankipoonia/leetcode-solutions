class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Get the length of the input list
        l = len(nums)
        # Iterate from the end of the list to the beginning (index 0)
        # This allows safe removal of elements without index shifting issues
        for i in range(l-1, -1, -1):
            # Check if the current element matches the value to remove
            if nums[i] == val:
                # Remove the element
                nums.pop(i)
        # Return the new length of the list after removals
        return len(nums)