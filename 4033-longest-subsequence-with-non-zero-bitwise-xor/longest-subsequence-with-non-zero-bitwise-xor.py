class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]

        for i in range(1, len(nums)):
            ans ^= nums[i]

        if ans == 0:
            if max(nums) == 0:
                return 0
            return len(nums) - 1

        return len(nums)