class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in arr2:
            while i in arr1:
                res.append(i)
                arr1.remove(i)
        return res + sorted(arr1)


sol = Solution()
arr1 = [28, 6, 22, 8, 44, 17]
arr2 = [22, 28, 8, 6]
print(sol.relativeSortArray(arr1, arr2))
