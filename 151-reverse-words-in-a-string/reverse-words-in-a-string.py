class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        text = s.split()
        text.reverse()

        str = list(text)

        s2 = ""
        inx = 0

        for i in range(len(str) - 1):
            s2 = s2 + str[inx] + " "
            inx += 1

        for i in range(0, 1):
            s2 = s2 + str[-1]

        return s2