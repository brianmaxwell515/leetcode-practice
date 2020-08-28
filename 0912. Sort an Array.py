class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(nums)


sol = Solution()
nums = [5, 1, 1, 2, 0, 0]
print(sol.sortArray(nums))
