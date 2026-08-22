class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        prodict = 1
        str_num = str(n)
        for i in range(len(str_num)):
            sum += int(str_num[i])
            prodict *= int(str_num[i])
        if n % (sum + prodict) == 0:
            return True
        return False

