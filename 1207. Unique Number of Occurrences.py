class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        res = []
        for i in set(arr):
            if arr.count(i) in res:
                return False
            else:
                res.append(arr.count(i))
        return True


sol = Solution()
arr = [1, 2, 2, 1, 1, 3]
print(sol.uniqueOccurrences(arr))
