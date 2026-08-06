class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list1 = []
        for num in nums:
            list1.append(nums.count(num))

        value = list1.index(1)

        return nums[value]