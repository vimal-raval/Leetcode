class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        if len(str_num) == 1:
            int_num = int(str_num)
            return int_num
        else:

            intlist = []
            for i in str_num:
                intlist.append(int(i))

            total = 0
            for i in range(len(intlist)):
                total += intlist[i]

            strlen = str(total)
            if len(strlen) == 0:
                intmain = int(strlen)
                return intmain
            elif len(strlen) != 0:
                num = int(strlen)
                return self.addDigits(num)