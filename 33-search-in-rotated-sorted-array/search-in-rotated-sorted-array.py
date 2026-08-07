class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        inx = 0
        if target in nums:
            for i in range(len(nums)):
                if target == nums[i]:
                    index += i
                    inx += 1
            return index
        else:
            return -1