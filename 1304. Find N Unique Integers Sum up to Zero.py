class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        if n % 2 == 1:
            res.append(0)
        for i in range(1, n//2+1):
            res.append(i)
            res.append(-i)
        return res


sol = Solution()
n = 5
print(sol.sumZero(n))
