class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = [min(i) for i in matrix]
        n = [max(i) for i in zip(*matrix)]
        return list(set(m) & set(n))


# matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
# matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
sol = Solution()
matrix = [[36376, 85652, 21002, 4510], [68246, 64237, 42962, 9974],
          [32768, 97721, 47338, 5841], [55103, 18179, 79062, 46542]]
print(sol.luckyNumbers(matrix))
