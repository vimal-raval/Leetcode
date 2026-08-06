class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list1 = []
        Ans_list = []
        for num in nums:
            list1.append(nums.count(num))

        for i in range(len(list1)):
            if list1[i] == 1:
                Ans_list.append(nums[i])

        return Ans_list