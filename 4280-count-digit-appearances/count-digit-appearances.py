class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        strr = ""
        for i in range(len(nums)):
            strr += str(nums[i])

        str_list = []

        for i in range(len(strr)):
            str_list.append(strr[i])

        num = str(digit)
        new_list = []

        for item in str_list:
            if item == num:
                new_list.append(item)

        length = len(new_list)
        return length