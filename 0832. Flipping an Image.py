class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for i in A:
            i.reverse()
            for j in range(len(i)):
                i[j] = abs(i[j]-1)
            res.append(i)
        return res


sol = Solution()
A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
print(sol.flipAndInvertImage(A))
