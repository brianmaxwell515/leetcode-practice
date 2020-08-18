class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        while num != 0:
            if num%2 == 0:
                num = num/2
            elif num%2 == 1:
                num -= 1
            res += 1
        return res

sol = Solution()
num = 8
print(sol.numberOfSteps(num))