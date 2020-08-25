class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        numi, numd = 0, len(S)
        for i in S:
            if i == "I":
                res.append(numi)
                numi += 1
            else:
                res.append(numd)
                numd -= 1
        res.append(numi)
        return res


S = "DDI"
print(Solution.diStringMatch(1, S))
