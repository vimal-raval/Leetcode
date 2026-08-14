class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        keypads = [[], [], [], [], [], [], [], []]
        length = []
        Ans = 0

        for i in range(len(word)):
            keypads[i % 8].append(word[i])

        for i in range(len(keypads)):
            if len(keypads[i]) == 0:
                length.append(0)
            elif len(keypads[i]) == 1:
                length.append(1)
            elif len(keypads[i]) == 2:
                length.append(1)
                length.append(2)
            elif len(keypads[i]) == 3:
                length.append(1)
                length.append(2)
                length.append(3)
            elif len(keypads[i]) == 4:
                length.append(1)
                length.append(2)
                length.append(3)
                length.append(4)

        for i in range(len(length)):
            Ans += length[i]

        return Ans