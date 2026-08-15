class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        
        elif s1 != s2:
            list_num = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    list_num.append(i)

            if len(list_num) != 2:
                return False

            s2_list = list(s2)
            s2_list[list_num[0]], s2_list[list_num[1]] = s2_list[list_num[1]], s2_list[list_num[0]]

            s = ''
            for i in range(len(s2_list)):
                s += s2_list[i]

            if s1 == s:
                return True

        return False