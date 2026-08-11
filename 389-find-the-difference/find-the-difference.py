class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        list1 = list(s)
        list2 = list(t)

        for i in range(len(list1)):
            if list1[i] in list2:
                list2.remove(list1[i])

        string = ''
        for i in range(len(list2)):
            string += list2[i]

        return string