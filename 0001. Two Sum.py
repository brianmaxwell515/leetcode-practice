class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in numMap:
                return [numMap.get(target - nums[i]), i]
            else:
                numMap[nums[i]] = i


nums = [2, 11, 15, 7]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))
