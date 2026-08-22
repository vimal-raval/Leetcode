class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        list_ans = []
        for i in range(1, max(target) + 1):
            if i in target:
                list_ans.append("Push")
            else:
                list_ans.append("Push")
                list_ans.append("Pop")

        return list_ans