class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)

        while 0 in nums:
            nums.remove(0)

        nums.extend([0] * count)