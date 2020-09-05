class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
m, n = 3, 3
sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)
