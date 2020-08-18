class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            res.append(sum(i > j for j in nums))
        return res


sol = Solution()
nums = [8, 1, 2, 2, 3]
print(sol.smallerNumbersThanCurrent(nums))

# Reference: https://stackoverflow.com/questions/10543303/number-of-values-in-a-list-greater-than-a-certain-number
