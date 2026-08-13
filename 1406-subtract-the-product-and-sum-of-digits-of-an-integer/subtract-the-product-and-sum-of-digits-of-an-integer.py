class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_num = str(n)
        Product = 1
        sum = 0
        for i in range(len(str_num)):
            Product *= int(str_num[i])
            sum += int(str_num[i])
        return (Product - sum)