class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.sort()
        resdict = {}
        res = []
        for i in arr:
            numcount = bin(i).count("1")
            resdict[numcount] = resdict.get(numcount, [])+[i]
        for j in resdict:
            res += resdict[j]
        return res


arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
print(Solution.sortByBits(1, arr))
