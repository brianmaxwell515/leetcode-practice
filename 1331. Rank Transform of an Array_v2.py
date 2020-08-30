class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        # Sort the "arr" list
        templist = sorted(set(arr))

        # Create the dict type for sorted "arr" list
        tempdict = {num: index+1 for index, num in enumerate(templist)}

        # Find and put the sorted number index into "res"
        for i in arr:
            res.append(tempdict[i])
        return res


sol = Solution()
arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
print(sol.arrayRankTransform(arr))
