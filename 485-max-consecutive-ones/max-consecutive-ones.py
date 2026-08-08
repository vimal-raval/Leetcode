class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list1 = []
        value = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                value += 1
            elif nums[i] == 0:
                list1.append(value)
                value *= 0
        list1.append(value)

        max_num = max(list1)
        return max_num