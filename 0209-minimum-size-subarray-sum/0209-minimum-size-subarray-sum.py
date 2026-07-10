class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0                  # Left pointer of the sliding window
        current_sum = 0           # Stores the sum of the current window
        min_length = float('inf') # Initially assume no valid window exists

        # Move the right pointer one step at a time
        for right in range(len(nums)):

            # Include the current element in the window
            current_sum += nums[right]

            # If the current window sum is at least target,
            # try shrinking the window from the left
            while current_sum >= target:

                # Update the minimum length found so far
                min_length = min(min_length, right - left + 1)

                # Remove the leftmost element from the window
                current_sum -= nums[left]

                # Move the left pointer to shrink the window
                left += 1

        # If no valid subarray was found, return 0
        if min_length == float('inf'):
            return 0

        return min_length

        