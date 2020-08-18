class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for i in J:
            res += S.count(i)
        return res

sol = Solution()
J = "aA"
S = "aAAbbbb"
print (sol.numJewelsInStones(J, S))