class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lenthh = len(nums)
        
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
            lenthh = len(nums)

        return lenthh