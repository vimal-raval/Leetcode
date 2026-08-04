class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Missing_num = []

        for i in range(min(nums), max(nums)):
            if i in nums:
                pass
            else:
                Missing_num.append(i)
        return Missing_num