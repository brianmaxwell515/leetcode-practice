class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 0
        n = str(n)
        for i in range(len(n)):
            a *= int(n[i])
            b += int(n[i])
        return a-b


sol = Solution()
n = 234
print(sol.subtractProductAndSum(n))
