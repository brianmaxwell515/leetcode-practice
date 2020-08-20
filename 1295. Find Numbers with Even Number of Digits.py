class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                res += 1
        return res


nums = [12, 345, 2, 6, 7896]
print(Solution.findNumbers(1, nums))
