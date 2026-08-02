class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        new_str = []

        inx = -1
        for i in range(len(s) - 1, -1, -1):
            new_str.append(s[i])
            inx += -1

        s[:] = new_str   