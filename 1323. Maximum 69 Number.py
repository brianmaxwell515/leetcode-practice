class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        return str(num).replace('6', '9', 1)


sol = Solution()
num = 9996
print(sol.maximum69Number(num))
