class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res, even, odd = [], [], []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])
        return res


sol = Solution()
A = [4, 2, 5, 7]
print(sol.sortArrayByParityII(A))
