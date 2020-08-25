class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        for i in A:
            B.append(i**2)
        return sorted(B)


A = [-4, -1, 0, 3, 10]
print(Solution().sortedSquares(A))
