class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str1 = str(x)

        if "-" in str1:
            str_list1 = []
            for i in range(len(str1)):
                str_list1.append(str1[i])

            str_list1.pop(0)
            num1 = ""
            for i in range(1, len(str_list1) + 1):
                num1 += str_list1[-i]
            ans = (int(num1) * (-1))
        else:
            str_list2 = []
            for i in range(len(str1)):
                str_list2.append(str1[i])

            num1 = ""
            for i in range(1, len(str_list2) + 1):
                num1 += str_list2[-i]

            ans = int(num1)

        if ans < -2147483648 or ans > 2147483647:
            return 0

        return ans