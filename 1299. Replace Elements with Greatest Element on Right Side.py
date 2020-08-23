class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxnum = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = maxnum
            maxnum = max(maxnum, temp)
        return arr


arr = [17, 18, 5, 4, 6, 1]
print(Solution.replaceElements(1, arr))
