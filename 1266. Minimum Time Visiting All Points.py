class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)-1):
            res += max(abs(points[i][0] - points[i+1][0]),
                       abs(points[i][1] - points[i+1][1]))
        return res


sol = Solution()
points = [[1, 1], [3, 4], [-1, 0]]
print(sol.minTimeToVisitAllPoints(points))
