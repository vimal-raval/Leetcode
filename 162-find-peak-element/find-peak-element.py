class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                return i
            
        return length - 1