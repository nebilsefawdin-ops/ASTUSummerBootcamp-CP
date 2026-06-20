class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = 0
        ans = 0

        while left < n:
            if nums[left] % 2 == 0 and nums[left] <= threshold:
                right = left
                while (right + 1 < n and
                       nums[right + 1] <= threshold and
                       nums[right + 1] % 2 != nums[right] % 2):
                    right += 1
                ans = max(ans, right - left + 1)              
                left = right
            left += 1

        return ans