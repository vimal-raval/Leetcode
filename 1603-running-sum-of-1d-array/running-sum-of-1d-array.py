class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        else:
            list1 = []
            list1.append(nums[0])
            num = 1
            for i in range(len(nums)):
                list1.append(list1[i] + nums[num])
                if len(list1) == len(nums):
                    break
                else:
                    num += 1

            return list1