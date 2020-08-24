class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')


sol = Solution()
x, y = 3, 1
print(sol.hammingDistance(x, y))
