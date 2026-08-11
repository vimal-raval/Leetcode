class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list1 = []
        num = nums[0]
        for i in range(len(nums)):
            if nums[i] == num:
                list1.append(nums[i])
                num += 1
            else:
                break
                
        sum_num = 0
        for i in range(len(list1)):
            sum_num += list1[i]

        while sum_num in nums:
            sum_num += 1

        return sum_num