class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        list1 = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                list1.append(nums1[i])

        set1 = set(list1)
        return list(set1)