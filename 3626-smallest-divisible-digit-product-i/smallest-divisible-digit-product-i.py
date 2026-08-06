class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        str_num = str(n)
        num = 1

        for ch in str_num:
            num *= int(ch)

        if num % t == 0:
            return n
        else:
            return self.smallestNumber(n + 1, t)