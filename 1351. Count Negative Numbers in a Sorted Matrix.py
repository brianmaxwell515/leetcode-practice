class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in grid:
            res += sum(j < 0 for j in i)
        return res


sol = Solution()
grid = [[3, 2], [1, 0]]
print(sol.countNegatives(grid))
