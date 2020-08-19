class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res


sol = Solution()
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
print(sol.createTargetArray(nums, index))
