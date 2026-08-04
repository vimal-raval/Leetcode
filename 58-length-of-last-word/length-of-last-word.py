class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        j = ''
        if len(s) == 1:
            return 1
        elif s.endswith(" ") == False:
            for i in range(1, len(s) + 1):
                if s[-i] != " ":
                    j += s[-i]
                else:
                    break
            return len(j)
        else:
            new = s.rstrip()
            for i in range(1, len(new) + 1):
                if new[-i] != " ":
                    j += new[-i]
                else:
                    break
            return len(j)