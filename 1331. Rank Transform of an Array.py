class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        tempdict = {}
        templist = arr[:]
        templist = sorted(set(templist))

        for i in range(len(templist)):
            tempdict[templist[i]] = i+1

        for j in arr:
            res.append(tempdict[j])

        return res


sol = Solution()
arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
print(sol.arrayRankTransform(arr))
