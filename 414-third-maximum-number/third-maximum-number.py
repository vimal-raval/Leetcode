class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = set(nums)
        nums1 = list(set1)

        if len(nums1) <= 2 :
            return (max(nums1))
        else:
            for i in range(0, 2):
                nums1.remove(max(nums1))
            return (max(nums1))